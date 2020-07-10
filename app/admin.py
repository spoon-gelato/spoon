from django.contrib import admin
from .models import Order, Cart, SizeItem, FlavorItem, OptionItem

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(SizeItem)
admin.site.register(FlavorItem)
admin.site.register(OptionItem)