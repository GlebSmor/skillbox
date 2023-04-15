from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse
from django.urls import reverse, reverse_lazy


def login_view(request: HttpRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/admin/')
        else:
            return render(request, 'myauth/login.html')
        
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return redirect('/admin/')
    
    return render(request, 'myauth/login.html', {'error': 'Invalid login credentials'})

class MyLogoutView(LogoutView):
    next_page = reverse_lazy('myauth:login')

def set_cookie_view(request: HttpRequest):
    response = HttpResponse('cookies se')
    response.set_cookie('fizz', 'buzz', max_age=3600)
    
    return response

def get_cookie_view(request: HttpRequest):
    value =request.COOKIES.get('fizz', 'default value')
    return HttpResponse(f'Cookie values: {value!r}')
    
def set_session_view(request: HttpRequest):
    request.session['foobar'] = 'spameggs'
    return HttpResponse('Session set')

def get_session_view(request: HttpRequest):
    value = request.session.get('foobar', 'default')
    return HttpResponse(f'Session value {value!r}')