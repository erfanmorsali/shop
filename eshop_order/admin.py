from django.contrib import admin
from .models import Order, OrderDetail


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_paid', 'payment_date']
    list_editable = ['is_paid']

    class Meta:
        Model = Order


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'order', 'price', 'count', 'is_send']
    list_filter = ['is_send']
    list_editable = ['is_send']

    class Meta:
        Model = OrderDetail


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
