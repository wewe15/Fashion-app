from rest_framework import serializers

from ..models import Order, OrderItem
from shop.models import Product


class OrderSerilizers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("id", "first_name", "last_name", "email",
                  "address", "postal_code", "city", "paid",
        )
        read_only_fields = ("id",)


class OrderItemSerilizers(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('id',  "order", 'product', 'price', 'quantity')
        read_only_fields = ('id',)
