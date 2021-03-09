from django.contrib import admin
from .models import Problem, Category


class AdminProblem(admin.ModelAdmin):
    list_display = ['title', 'points', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Category, AdminCategory)
admin.site.register(Problem, AdminProblem)