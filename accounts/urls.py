from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile
from accounts import url_reset

"""
********************************************************************

ORIGINAL CODE IN THIS FILE COPIED FROM:

https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation/tree/master/07-CustomAuthentication/01-email_authentication/accounts

********************************************************************
"""

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset))
]
