from django.urls import path
from .views import ProductListView, ProductDetailView, SearchResultListView


urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("products/<int:category>", ProductListView.as_view(), name="product_list"),
    path("<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("search/", SearchResultListView.as_view(), name="search_result")
]
