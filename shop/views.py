from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.db.models import Q

from .models import Product
from cart.forms import CartAddProductForm


class ProductListView(LoginRequiredMixin, ListView): 
    model = Product
    context_object_name = "products_list" 
    template_name = "products/product_list.html"
    login_url = 'login'

    def get_queryset(self):
        category = self.kwargs.get('category')
        if category:
            return Product.objects.filter(category=category) 
        return Product.objects.all()

class ProductDetailView(LoginRequiredMixin, FormMixin, DetailView): 
    model = Product
    context_object_name = "product"
    form_class = CartAddProductForm
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
