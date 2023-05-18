from django.contrib.syndication.views import Feed
from django.http import HttpResponseRedirect
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy, reverse
from .models import News  
  
  
class LatestNewsFeed(Feed):  
    title = 'News'  
    link = '/houseshop/'  
    description = 'Latest news'  
    def items(self):  
        return News.objects.all()[:5]  
      
    def item_title(self, item: News):  
        return item.title  
      
    def item_description(self, item: News):  
        return truncatewords(item.text, 30)
    
    def item_link(self, item: News):
        return reverse('houseshop:news_detail', args=[item.pk])