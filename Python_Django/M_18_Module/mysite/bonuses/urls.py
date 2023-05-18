from django.urls import path

from django.contrib.auth.views import LoginView
from .views import RegisterView, PersonalAccount, MyLogoutView, BalanceView, home


app_name = 'auth'


urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(
        template_name="bonuses/login.html",
        redirect_authenticated_user=True,), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('account/', PersonalAccount.as_view(), name='account'),
    path('account/<int:pk>/balance/', BalanceView.as_view(), name='balance'),
]