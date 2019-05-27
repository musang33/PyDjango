from django.db import models

# Create your models here.

class LatestInfoTbl(models.Model) :
    fileName = models.CharField(max_length=200)
    pubDate = models.CharField(max_length=200)

    def __str__(self):
        return self.fileName


class RssDataTbl(models.Model) :
    no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pubDate = models.CharField(max_length=200)
    article = models.CharField(max_length=2000)

    def __str__(self):
        return self.title

