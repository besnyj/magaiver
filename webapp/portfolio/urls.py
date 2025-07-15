from django.urls import path

from . import views

urlpatterns = [
    path('', views.portfolio_upload, name="portfolio_upload"),
    path('display', views.portfolio_display, name="portfolio_display")
]