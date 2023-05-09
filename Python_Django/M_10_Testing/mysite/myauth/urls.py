from django.urls import path
from django.contrib.auth.views import LoginView

from .views import (
    AboutMeView, RegisterView,MyLogoutView, 
    get_cookie_view, FooBarView
)

app_name = "myauth"

urlpatterns = [
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("register/", RegisterView.as_view(), name="register"),
    path('login/', 
         LoginView.as_view(template_name='myauth/login.html', 
                           redirect_authenticated_user=True), 
         name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('cookie/get/', get_cookie_view, name='get-cookie'),
    path('foo-bar/', FooBarView.as_view(), name='foo-bar'),

]
