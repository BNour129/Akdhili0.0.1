from django.urls import re_path, include, path
from .views import about_view, contact_view, error_view
from . import views
from sprint1.views import homepage_view

app_name = 'pages'

urlpatterns = [
    path('home/', homepage_view, name="home"),
    path('contact/',contact_view, name="contact"),
    path('about/', about_view, name="about"),
    path('', error_view, name="error"),
]
