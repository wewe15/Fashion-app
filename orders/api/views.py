from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import OrderSerilizers, OrderItemSerilizers
from ..models import Order, OrderItem


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerilizers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
