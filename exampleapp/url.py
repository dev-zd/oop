from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_department/', views.add_department, name='add_department'),

]