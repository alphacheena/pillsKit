from django.urls import path, include
from rest_framework import routers
from .views import UserRegistrationView, UserView, UserUpdateView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('register', UserRegistrationView.as_view(), name='register'),
    path('user', UserView.as_view(), name='account'),
    path('user/update/<int:id>', UserUpdateView.as_view(), name='userUpdate'),
]
