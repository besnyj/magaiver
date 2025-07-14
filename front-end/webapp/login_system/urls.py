from django.urls import path
from rest_framework.urls import urlpatterns

from . import views

urlpatterns = [
    path('', views.login_user, name="login"),
]
