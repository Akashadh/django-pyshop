from django.contrib import admin
from .models import product, offer

# Register your models here.


class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(product, productAdmin)
admin.site.register(offer)
