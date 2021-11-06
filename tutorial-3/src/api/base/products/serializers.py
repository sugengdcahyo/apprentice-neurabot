from products.models import Product, Type
from rest_framework import serializers

class TypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'
class ProductSerializers(serializers.ModelSerializer):
    type = TypeSerializers()
    class Meta:
        model = Product
        fields = '__all__'