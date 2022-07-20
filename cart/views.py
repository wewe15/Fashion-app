from django.urls import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect, render

from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


class CartAddView(ListView):
    model = Product
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(
                product=product, quantity=cd["quantity"], override_quantity=cd["override"]
            )
        return redirect("cart:cart_detail")


class CartRemoveView(ListView):
    model = Product
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect("cart:cart_detail")


class CartDetailView(ListView):
    model = Product
    def get(self, request):
        cart = Cart(request)
        for item in cart:
            item["update_quantity_form"] = CartAddProductForm(
                initial={"quantity": item["quantity"], "override": True}
            )
        return render(request, "cart/cart_detail.html", {"cart": cart})
