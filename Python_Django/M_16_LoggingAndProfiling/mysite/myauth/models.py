from django.contrib.auth.models import User
from django.db import models


def avatar_dir(instanse, filename):
    return "profiles/profile_{pk}/avatar/{filename}".format(
        pk=instanse.pk,
        filename=filename
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    agreement_accepted = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True, upload_to=avatar_dir)
