from django.urls import path
from .views import AddToCartView, CartDetailView, OrderDetailView, CheckOutView, CartView

urlpatterns = [
    path('<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('orders/', OrderDetailView.as_view(), name='order_detail'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('cart/', CartView.as_view(), name='cart'),
]
