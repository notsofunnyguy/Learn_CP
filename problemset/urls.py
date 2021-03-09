from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='problemset-home'),
    path('ide/', views.ide, name='online-ide'),
    path('run/', views.run, name='run-code'),
    path('problem/<int:pk>', views.problem, name='problemset-problem')
]