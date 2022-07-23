from rest_framework import serializers

from ..models import Product, Category


class CategorySerilizers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ("id", "name")
        read_only_fields = ("id",)


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = ('id',  "category", 'name', 'image', 'description', 'price', 'available')
        read_only_fields = ('id',)
