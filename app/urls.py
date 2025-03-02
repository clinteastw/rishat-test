from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:id>/', views.get_item, name='item_detail'),
    path('buy/<int:id>/', views.buy_item, name='buy_item'),
    path('order/<int:id>/', views.get_order, name='order_detail'),
    path('buy_order/<int:id>/', views.buy_order, name='buy_order'),
    path('', views.home, name='home'),
    path('cancel/', views.cancel, name='cancel'),
    path('success/', views.success, name='success'),
]