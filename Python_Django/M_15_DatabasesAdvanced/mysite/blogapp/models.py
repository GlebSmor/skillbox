from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, null=False)
    bio = models.TextField(null=False, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=40, null=False)


class Tag(models.Model):
    name = models.CharField(max_length=20, null=False)


class Article(models.Model):
    title = models.CharField(max_length=20, null=False)
    content = models.TextField(null=False, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    tags = models.ManyToManyField(Tag, related_name="tags", null=False)
    