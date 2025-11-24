from django.urls import path
from . import views

urlpatterns = [
    path('', views.houses_list, name='houses_list'),
    path('<str:house_id>/', views.house_detail, name='house_detail'),
]
