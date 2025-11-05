from django.urls import path
from . import views

urlpatterns = [
    path('drinks/', views.list_drinks, name='drinks-list'),
    path('recommend/', views.recommend, name='recommend'),
    path('form/', views.recommend_form_view, name='recommend_form'),
]