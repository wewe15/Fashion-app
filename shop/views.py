from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Product


class ProductListView(LoginRequiredMixin, ListView): 
    model = Product
    context_object_name = "products_list" 
    template_name = "products/product_list.html"
    login_url = 'login' 


class ProductDetailView(LoginRequiredMixin, DetailView): 
    model = Product
    context_object_name = "product"
    template_name = "products/product_detail.html"
    login_url = 'login' 


class SearchResultListView(ListView):
    model = Product
    context_object_name = "products_list"
    template_name = "products/search_result.html"
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(
            Q(name__icontains=query) | Q(price__icontains=query)
        )
