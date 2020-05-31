from django.conf.urls import url
from .views import checkout

"""
********************************************************************

ORIGINAL CODE IN THIS FILE COPIED FROM:

https://github.com/Code-Institute-Solutions/PuttingItAllTogether-Ecommerce/tree/master/03-HostingYourEcommerceWebApp/07-heroku_hosting/checkout

********************************************************************
"""

urlpatterns = [
    url(r'^(?P<id>\d+)/$', checkout, name='checkout'),
]
