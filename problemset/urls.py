from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='problemset-home'),
    path('register/', views.register, name='problemset-register'),
    path('problem/', views.problem, name='problemset-problem'),
    path('submit/', views.submitcode, name='problemset-submit_code'),
    path('discussions/', views.discussions, name='problemset-discussions'),
    path('ide/', views.ide, name='online-ide'),
    path('run/', views.run, name='run-code')
]