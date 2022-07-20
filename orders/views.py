from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views import generic

from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart



class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = OrderCreateForm
    template_name = 'orders/order_create.html'
    login_url = 'login'
        
    def post(self, request):
        cart = Cart(request)
        form = OrderCreateForm(request.POST)
        order = form.save()
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        return redirect('home')
    
