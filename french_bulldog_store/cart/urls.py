from django.urls import path

from french_bulldog_store.cart.views import Cart, Checkout

urlpatterns = (
    path('', Cart.as_view(), name="cart"),
    path('checkout/', Checkout.as_view(), name="checkout"),


)