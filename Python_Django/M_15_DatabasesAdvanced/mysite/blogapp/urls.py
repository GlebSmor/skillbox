from .views import ListArticlesView
from django.urls import path, include

app_name = 'bloagapp'

urlpatterns = [
    path("articles/", ListArticlesView.as_view(), name="articles_list"),
]