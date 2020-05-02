
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # path(r'^', include(router.urls)),
    path(r'auth/', include('rest_auth.urls')),
    path(r'register/', include('rest_auth.registration.urls')),
    path(r'users/', views.user_list),
]