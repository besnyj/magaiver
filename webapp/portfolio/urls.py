from django.urls import path

from . import views

urlpatterns = [
    path('', views.portfolio_upload, name="portfolio_upload"),
]