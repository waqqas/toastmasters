from django.urls import include, path

from .views import ModelViewSet

model_list = ModelViewSet.as_view(
    {
        "get": "list",
        "post": "create",
        "delete": "destroy_list",
        "put": "update_list",
    }
)
model_details = ModelViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)

urlpatterns = [
    path("<str:model>/", model_list, name="model_api_model_list"),
    path("<str:model>/<str:id>", model_details, name="model_api_model_details"),
]
