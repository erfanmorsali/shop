from django.contrib import admin
from .models import ContactUs


# Register your models here.

class MoodelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'full_name', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['subject', 'full_name']

    class Meta:
        model = ContactUs


admin.site.register(ContactUs, MoodelAdmin)
