from django.shortcuts import render

# Create your views here.
from math import prod
from rest_framework import status
from .models import  Order, OrderItem, Product
from .serializers import  OrderSerializer, OrderItemSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import Http404

class getOrderDetails(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format = None):
        user = request.user
        order = Order.objects.filter(user=user).first()
        print(order.total_price)
        queryset = OrderItem.objects.filter(order=order)
        serializer = OrderItemSerializer(queryset, many = True)
        return Response(serializer.data)

class createOrder(APIView):
    def post(self, request, format=None):
        user = request.user
        order = Order.objects.create(user = user)
        data = request.data
        product = Product.objects.get(id = data.get('product'))
        price = product.price
        quantity = data.get('quantity')
        orderItem = OrderItem(user = user, product = product, order = order, quantity = quantity, price = price)
        orderItem.save()
        totalPrice = 0
        totalPrice = quantity * price
        order.total_price = totalPrice
        print(totalPrice)
        order.save()
        return Response({'success' : 'New Order Created'})

class getObject():
    def get_object(pk):
        try:
            obj = Order.objects.get(pk=pk)
            return obj
        except Order.DoesNotExist:
            raise Http404



class updateOrder(APIView):
    def put(self, request, format=None):
        pass
        # user = request.user
        # order = Order.objects.update(user = user)
        # data = request.data
        # product = Product.objects.get(id = data.get('product'))
        # price = product.price
        # quantity = data.get('quantity')
        # orderItem = OrderItem(user = user, product = product, order = order, quantity = quantity, price = price)
        # orderItem.save()
        # totalPrice = 0
        # totalPrice = quantity * price
        # order.total_price = totalPrice
        # print(totalPrice)
        # order.save()
        # return Response({'success' : 'New Item Added to product'})
