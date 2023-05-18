from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache

from .models import Profile
from shop.models import Order


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "bonuses/register.html"
    success_url = reverse_lazy("bonuses:account")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response
    
    
class PersonalAccount(LoginRequiredMixin, TemplateView):
    template_name = "bonuses/account.html"
    queryset = Profile.objects.prefetch_related("promotions")
    def set_cache(self):
        cache_key = f'promotions:{self.request.user.username}'
        promotions = self.request.user.profile.promotions
        
        cache.set({cache_key:promotions})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user_id=self.request.user.id)
        return context


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("bonuses:login")
    
    
def home(request):
    return render(request, 'shop/home.html')


class BalanceView(UpdateView):
    model = Profile
    fields = "balance",
    template_name_suffix = "_update"
    
    def get_success_url(self):
        return reverse("bonuses:account")