from rest_framework import serializers
from .models import FoodType, Food, Comment
from django.contrib.auth import get_user_model



User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username']

class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ['id', 'nomi']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'food_type', 'nomi', 'tarkibi', 'narxi']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'food', 'author', 'created']