from django.urls import path
from . import views

urlpatterns = [
    path('',views.item,name='item'),
    path('updateItem/<str:pk>/',views.updateItem,name='updateItem'),
    path('deleteItem/<str:pk>/',views.deleteItem,name='deleteItem')
]