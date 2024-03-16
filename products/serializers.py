from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

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

class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, user):
        token, _ = Token.objects.get_or_create(user=user)

        return token.key
    
    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'token')
