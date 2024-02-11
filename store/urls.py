from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('detail/', views.detail, name='detail'),
    path('shop/', views.shop, name='shop'),

    path('testall/testDetail/<int:id>', views.testDetail, name='testDetail'),
    path('testall/', views.testall, name='testall'),



    path('shop/cart/', views.cart, name='cart'),
    path('shop/checkout/', views.checkout, name='checkout'),
    path('shop/contact/', views.contact, name='contact'),
    path('shop/detail/', views.detail, name='detail'),


]