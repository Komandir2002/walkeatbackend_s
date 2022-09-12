from rest_framework.pagination import PageNumberPagination


class FitPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 1000
    page_query_param = "page_size"
