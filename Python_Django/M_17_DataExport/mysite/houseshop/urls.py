from django.urls import path
from .views import SalesListView, NewsView, NewsDetailView, home_page, contacts, about_us
from .feeds import LatestNewsFeed
from django.contrib.sitemaps.views import sitemap
from .sitemap import NewsSitemap

app_name = 'houseshop'

sitemaps = {
    "news": NewsSitemap
}

urlpatterns = [
    path("", home_page, name="home"),
    path("about-us/", about_us, name="about_us"),
    path("for-sale/", SalesListView.as_view(), name="sale_list"),
    path("contacts/", contacts, name="contacts"),
    path("news/", NewsView.as_view(), name="news"),
    path("news/<int:pk>/", NewsDetailView.as_view(), name="news_detail"),
    path("feed/", LatestNewsFeed(), name="news_feed"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps},
         name="django.conrib.sitemaps.views.sitemap")
]