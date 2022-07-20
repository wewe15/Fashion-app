from django.shortcuts import redirect
from django.views import generic

from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart



class OrderCreateView(generic.CreateView):
    form_class = OrderCreateForm
    template_name = 'orders/order_create.html'
        
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
    
