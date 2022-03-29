# backend/server/server/urls.py
from django.contrib import admin
from django.urls import path

from apps.accounts.urls import accounts_urlpatterns
from apps.gig.urls import gig_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += accounts_urlpatterns # add URLs for authentication
urlpatterns += gig_urlpatterns    # notes URLs