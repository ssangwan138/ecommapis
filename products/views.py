from math import prod
from rest_framework import status
from .models import  Product
from .serializers import  ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

class getProductsList(APIView):
    def get(self, pgno, format = None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    

class createProduct(APIView):
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class getObject():
    def get_object(pk):
        try:
            obj = Product.objects.get(pk=pk)
            return obj
        except Product.DoesNotExist:
            raise Http404


class getProductDetails(APIView):
    def get(self, request, pk):
        product = getObject.get_object(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class updateProduct(APIView):
    def put(self, request, pk, format=None):
        product = getObject.get_object(pk=pk)
        # data = request.data
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            # serializer.save()
            print(request.data.keys())
            serializer.save(update_fields=list(request.data.keys())) 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class deleteProduct(APIView):
    def delete(self, request, pk, format=None):
        product = getObject.get_object(pk=pk)
        id = product.pk
        product.delete()
        return Response({"id": id, "deletion" : "successfull"}, status=status.HTTP_204_NO_CONTENT)




