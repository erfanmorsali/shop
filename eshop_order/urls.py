from django.urls import path

from eshop_order.views import add_user_order, user_order_items, delete_user_order, send_request, verify

urlpatterns = [
    path('add-user-order', add_user_order, name='add_user_order'),
    path('order-items', user_order_items, name='order-items'),
    path('delete-user-order/<item_id>', delete_user_order, name='delete-user-order'),
    path('request', send_request, name='request'),
    path('verify', verify, name='verify'),
]
