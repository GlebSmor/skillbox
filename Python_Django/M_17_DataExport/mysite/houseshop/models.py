from django.db import models
from django.urls import reverse


class HouseType(models.Model):
    name = models.CharField(max_length=100, null=False)
    
    class Meta:
        ordering = ["pk",]
        verbose_name = "Type"
        verbose_name_plural = "Types"
        
    def __str__(self):
        return str(self.name)


class RoomsCount(models.Model):
    count = models.IntegerField()
    
    class Meta:
        ordering = ["pk",]
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        
    def __str__(self):
        return str(self.count)


class News(models.Model):
    title = models.CharField(max_length=20, null=False)
    text = models.TextField(null=False, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=False)
    
    def get_absolute_url(self):
        return reverse("houseshop:news_detail", args=[str(self.pk)])
    
    
    class Meta:
        ordering = ["pk",]
        verbose_name = "News"
        verbose_name_plural = "News"
        
    def __str__(self):
        return str(self.title)


class House(models.Model):
    name = models.CharField(max_length=100, null=False, default="House")
    address = models.CharField(max_length=200, null=False)
    price = models.DecimalField(default=0, max_digits=100, decimal_places=2)
    date_of_const = models.DateField(null=True)
    rooms = models.ForeignKey(RoomsCount, on_delete=models.PROTECT)
    type = models.ForeignKey(HouseType, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ["pk",]
        verbose_name = "House"
        verbose_name_plural = "Houses"
        
    def __str__(self):
        return str(self.name)
        
        