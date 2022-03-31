from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.conf import settings
from box.models import Box
from order.models import Component, Order, Product

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Box
        fields = ['id','name', "price"]
class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Component
        fields = ['price' , "name"]

class ProductSerializer(serializers.ModelSerializer):
    component = ComponentSerializer(many=True, read_only=True)
    box = BoxSerializer( read_only=True)
    class Meta:
        model=Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model=Order
        fields = ['name', "price", 'purchaser','product']
        
