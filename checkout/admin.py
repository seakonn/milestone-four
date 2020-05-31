from django.contrib import admin
from .models import Order, OrderLineItem

"""
********************************************************************

ORIGINAL CODE IN THIS FILE COPIED FROM:

https://github.com/Code-Institute-Solutions/PuttingItAllTogether-Ecommerce/tree/master/03-HostingYourEcommerceWebApp/07-heroku_hosting/checkout

********************************************************************
"""


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )


admin.site.register(Order, OrderAdmin)
