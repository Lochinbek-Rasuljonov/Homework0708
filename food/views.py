from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import FoodType, Food, Comment
from .serializers import FoodTypeSerializer, FoodSerializer, CommentSerializer



class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
