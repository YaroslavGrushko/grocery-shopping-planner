from rest_framework import serializers

from products.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = ("id", "user", "name")
    
    def validate(self, attrs):
        if len(attrs["name"]) == 0:
            raise serializers.ValidationError("Ім'я категорії не може бути пустим")
        return attrs


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity', 'price', 'category')

class ProductViewSerializer(ProductSerializer):
    # get Product with whole Category for read
    category = CategorySerializer()