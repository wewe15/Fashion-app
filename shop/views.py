from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.db.models import Q

from .models import Product
from cart.forms import CartAddProductForm


class ProductListView(ListView): 
    model = Product
    context_object_name = "products_list" 
    template_name = "products/product_list.html"

    def get_queryset(self):
        category = self.kwargs.get('category')
        if category:
            return Product.objects.filter(category=category) 
        return Product.objects.all()

class ProductDetailView(FormMixin, DetailView): 
    model = Product
    context_object_name = "product"
    form_class = CartAddProductForm
    template_name = "products/product_detail.html"


class SearchResultListView(ListView):
    model = Product
    context_object_name = "products_list"
    template_name = "products/search_result.html"
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(
            Q(name__icontains=query) | Q(price__icontains=query)
        )
