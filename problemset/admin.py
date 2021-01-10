from django.contrib import admin
from .models import Problem, Category, User

class AdminProblem(admin.ModelAdmin):
    list_display = ['title', 'points', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['title']

class AdminUser(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username']

admin.site.register(Category, AdminCategory)
admin.site.register(Problem, AdminProblem)
admin.site.register(User, AdminUser)

