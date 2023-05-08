from django.contrib import admin
from django.urls import path
from accounts.urls import urlpatterns as accounts_urlpatterns
from kits.urls import urlpatterns as kits_urlpatterns

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += accounts_urlpatterns
urlpatterns += kits_urlpatterns
