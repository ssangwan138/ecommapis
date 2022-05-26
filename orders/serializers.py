from dataclasses import field
from rest_framework import serializers
from orders.models import Order, OrderItem
from products.models import Product
from products.serializers import ProductSerializer


class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.Serializer):
    product = ProductSerializer()
    order = OrderSerializer()
    class Meta:
        model = OrderItem
        fields = ['user', 'product', 'price', 'quantity']