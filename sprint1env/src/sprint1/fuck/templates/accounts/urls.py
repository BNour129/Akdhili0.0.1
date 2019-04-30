from django.urls import path
from django.conf.urls import url
from users.views import account_details_view, login_view, signup_view, logout_view
from . import views
from sprint1.views import homepage_vie


app_name = 'users'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('signup/', signup_view, name="signup"),
    path('logout/', logout_view, name="logout"),
    path('details/', account_details_view, name= "details"),
    path('',homepage_view, name="home"),
]
