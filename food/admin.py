from django.contrib import admin
from .models import CustomUser, FoodType, Food, Comment
from django.contrib.auth.admin import UserAdmin



admin.site.register(CustomUser, UserAdmin)

@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomi']

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'food_type', 'narxi']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'food', 'created']