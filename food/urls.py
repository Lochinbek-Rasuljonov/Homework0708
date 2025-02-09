from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodTypeViewSet, FoodViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'foodtypes', FoodTypeViewSet)
router.register(r'foods', FoodViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')), 
    path('auth/', include('djoser.urls.jwt')),  
]
