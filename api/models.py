from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.TextField(max_length=255)
    pmid = models.IntegerField()
    abstract = models.TextField(max_length=255)
    full_text_link = models.TextField(max_length=255)
    keywords = models.TextField(max_length=255)
