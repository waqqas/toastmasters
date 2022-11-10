from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class APIPagination(PageNumberPagination):
    page_size_query_param = "_page_size"

    def get_paginated_response(self, data):
        return Response(
            {
                "total": self.page.paginator.count,
                "current_page": self.page.number,
                "num_pages": self.page.paginator.num_pages,
                "per_page": self.page.paginator.per_page,
                "results": data,
            }
        )


class APISummaryPagination(PageNumberPagination):
    page_size = 1

    def get_paginated_response(self, data):
        return Response(
            {
                "total": self.page.paginator.count,
            }
        )


class ModelApiPagination(APIPagination):
    page_size = 100
