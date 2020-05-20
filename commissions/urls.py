from django.conf.urls import url
from .views import request_commission


urlpatterns = [
    url(r'^request/', request_commission, name="request_commission")
]
