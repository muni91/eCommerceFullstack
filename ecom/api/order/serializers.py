from django.db.models import fields
from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'product_names', 'total_products', 'total_amount', 'transaction_id')