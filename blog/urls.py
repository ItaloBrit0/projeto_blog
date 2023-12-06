from django.urls import path
from .import views


urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('post/<int:pk>/',views.blog_detalhe,name='blog_detalhe'),
    path('categoria/<categoria>', views.blog_categoria, name='blog_categoria'),
]

