from django.conf.urls import url
from .views import request_commission, display_commission


urlpatterns = [
    url(r'^request/', request_commission, name="request_commission"),
    url(r'^(?P<id>\d+)/$', display_commission, name="commission")
]
