from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Promotion(models.Model):
    
    title = models.CharField(max_length=100, null=False)
    text = models.TextField(null=False, blank=True)
    date = models.DateField(auto_now_add=True, null=False)

    class Meta:
        ordering = ["pk",]
        verbose_name = _("Promotion")
        verbose_name_plural = _("Promotions")
        
    def __str__(self):
        return str(self.title)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    balance = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    promotions = models.ManyToManyField(Promotion)

    
    class Meta:
        ordering = ["pk",]
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        
    def __str__(self):
        return str(self.user.username)

