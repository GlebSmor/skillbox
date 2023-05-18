from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class SalesListView(ListView):
    template_name = "houseshop/sale_list.html"
    context_object_name = "houses"
    queryset = House.objects.select_related('rooms', 'type')
    
   
class NewsView(ListView):
    template_name = "houseshop/news.html"
    context_object_name = "news"
    queryset = News.objects.all()
    
    
class NewsDetailView(DetailView):
    template_name = "houseshop/news_detail.html"
    model = News
    context_object_name = "news"
   
    
def home_page(request: HttpRequest):
    return render(request, 'houseshop/home.html')


def contacts(request: HttpRequest):
    return render(request, 'houseshop/contacts.html')


def about_us(request: HttpRequest):
    return render(request, 'houseshop/about_us.html')