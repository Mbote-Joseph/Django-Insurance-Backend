from django.shortcuts import render
from .models import Customer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CustomerSerializer
# Create your views here.
@api_view(['GET'])
def getCustomer(request):
    if request.method == 'GET':
        Customers = Customer.objects.all()
        serializer = CustomerSerializer(Customers, many=True)
        return Response(serializer.data)
    return Response(status=400)

@api_view(['POST'])
def postCustomer(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response(status=400)

@api_view(['PUT'])
def putCustomer(request, pk):
    if request.method == 'PUT':
        Customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(Customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    return Response(status=400)

@api_view(['DELETE'])
def deleteCustomer(request, pk):
    if request.method == 'DELETE':
        Customer = Customer.objects.get(pk=pk)
        Customer.delete()
        return Response(status=204)
    return Response(status=400)