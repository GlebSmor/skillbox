from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.translation import gettext_lazy as _, ngettext

import logging

logger = logging.getLogger(__name__)


class UserLoginView(LoginView):
    template_name="myauth/login.html"
    redirect_authenticated_user=True
    
    def get_success_url(self):
        logger.info(f'Пользователь {self.request.user.username} авторизовался')
        return self.get_redirect_url() or self.get_default_redirect_url()


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about-me")
    
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
    

class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")
    
    
class UsersList(ListView):
    template_name = "myauth/users-list.html"
    context_object_name = "profiles"
    queryset = Profile.objects.all()
    
    
class UserDetailsView(DetailView):
    template_name = "myauth/about-me.html"
    model = User
    context_object_name = "user"


class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ("avatar", )
    
    def test_func(self):
        if self.request.user.is_staff or self.request.user.pk == self.get_object().user_id:  
            return True
        else:
            return False
    

    def get_success_url(self):
        return reverse(
            "myauth:user_detail",
            kwargs={"pk": self.object.user.pk},
        )


@user_passes_test(lambda u: u.is_superuser)
def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)

    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default value")

    return HttpResponse(f"Cookie value: {value!r}")


@permission_required("myauth.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set!")


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")
    return HttpResponse(f"Session value: {value!r}")


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"foo": "bar", "spam": "eggs"})


class HelloView(View):
    msg = _("Hello world!")
    
    def get(self, request: HttpRequest):
        items = request.GET.get("items") or 0
        int_items = int(items)
        products = ngettext(
            "one product",
            "{count} products",
            int_items, 
        )
        products = products.format(count=int_items)
        return HttpResponse(f"<h1>{self.msg}</h1>"
                            f"\n<h2>{products}</h2>")