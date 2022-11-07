from re import split

from django.apps import apps
from django.conf import settings
from django.db import models
from django.db.models.expressions import F

# from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, serializers, status, viewsets
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey

from .paginations import APISummaryPagination, ModelApiPagination


class ModelViewSet(viewsets.ModelViewSet):
    permission_classes = (HasAPIKey,)
    lookup_field = "id"

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering = "id"

    @property
    def pagination_class(self):
        count_only = self.request.query_params.get("_count", "false").lower() == "true"
        if count_only:
            return APISummaryPagination
        else:
            return ModelApiPagination

    @property
    def filterset_fields(self):
        app_label, model_name = self.kwargs["model"].split(".")

        model_cls = apps.get_model(app_label, model_name)
        if issubclass(model_cls, models.Model):
            # filters for model fields
            fieldset = {
                field.name: [
                    "exact",
                    "gt",
                    "gte",
                    "lt",
                    "lte",
                    "in",
                    "iexact",
                    "startswith",
                    "istartswith",
                    "endswith",
                    "iendswith",
                    "regex",
                    "iregex",
                    "isnull",
                    "contains",
                    "icontains",
                    "ne",
                ]
                for field in [
                    field
                    for field in model_cls._meta.get_fields()
                    if field.get_internal_type()
                    not in [
                        "JSONField",
                        "ForeignKey",
                        "ManyToManyField",
                        "OneToOneField",
                        "StripeForeignKey",
                        "PaymentMethodForeignKey",
                    ]
                ]
            }

            # filters for model relations
            for field in [
                field
                for field in model_cls._meta.get_fields()
                if field.get_internal_type()
                in [
                    "ForeignKey",
                    "ManyToManyField",
                    "OneToOneField",
                    "StripeForeignKey",
                    "PaymentMethodForeignKey",
                ]
            ]:
                fieldset[field.name] = [
                    "exact",
                    "gt",
                    "gte",
                    "lt",
                    "lte",
                    "isnull",
                ]
            return fieldset
        else:
            return {}

    @property
    def ordering_fields(self):
        app_label, model_name = self.kwargs["model"].split(".")

        model_cls = apps.get_model(app_label, model_name)
        if issubclass(model_cls, models.Model):
            ordering_fields = [field.name for field in model_cls._meta.get_fields()]
            return ordering_fields
        else:
            return []

    def get_queryset(self):
        app_label, model_name = self.kwargs["model"].split(".")

        distinct_list = self.request.query_params.getlist("_distinct", [])
        prefetch = self.request.query_params.get("_prefetch", None)

        model_cls = apps.get_model(app_label, model_name)
        if issubclass(model_cls, models.Model):
            if distinct_list:
                self.ordering = None
                return (
                    model_cls.objects.distinct()
                    .values(*distinct_list)
                    .order_by(*distinct_list)
                )
            else:
                return model_cls.objects.all().prefetch_related(prefetch)
        else:
            return model_cls.objects.none()

    def get_serializer_class(self, *args, **kwargs):
        app_label, model_name = self.kwargs["model"].split(".")

        model_cls = apps.get_model(app_label, model_name)
        if issubclass(model_cls, models.Model):

            class ListSerializer(serializers.ListSerializer):
                def create(self, validated_data):
                    app_label, model_name = self.kwargs["model"].split(".")

                    model_cls = apps.get_model(app_label, model_name)
                    if issubclass(model_cls, models.Model):
                        ignore_conflicts_param = self.request.query_params.get(
                            "_ignore_conflicts", "false"
                        )
                        ignore_conflicts = (
                            True if ignore_conflicts_param.lower() == "true" else False
                        )

                        model_list = [model_cls(**item) for item in validated_data]
                        return model_cls.objects.bulk_create(
                            model_list, ignore_conflicts=ignore_conflicts
                        )
                    return []

            distinct_list = self.request.query_params.getlist("_distinct", [])

            class ModelSerializer(serializers.ModelSerializer):
                class Meta:
                    fields = "__all__" if not distinct_list else distinct_list
                    model = model_cls
                    list_serializer_class = ListSerializer

            return ModelSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        # if we have passed multiple objects to create
        if self.action == "create":
            kwargs["many"] = isinstance(kwargs["data"], list)
        return serializer_class(*args, **kwargs)

    def destroy_list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        self.perform_destroy_list(queryset)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy_list(self, queryset):
        queryset.delete()

    def update_list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        self.perform_update_list(queryset, request)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_update_list(self, queryset, request) -> int:
        data = {}
        for key, value in request.data.items():
            parts = split("(.*?)__(.*)", str(value) or "")
            if len(parts) == 4:
                data[key] = F(parts[2]) if parts[1] == "expr_f" else value
            else:
                data[key] = value

        return queryset.update(**data)

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        limit = self.request.query_params.get("_limit")
        if limit not in ["None", None]:
            return queryset[: int(limit)]
        else:
            return queryset
