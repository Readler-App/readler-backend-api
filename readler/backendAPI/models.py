from django.db import models
from django.contrib.postgres.fields import ArrayField
from cuser.models import AbstractCUser


# Abstraction layer on top of CUser
class CustomUser(AbstractCUser):
    middleNames = models.CharField(max_length=100)
    username = models.CharField(max_length=50, default='')


class Settings(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fontFamily = models.CharField(max_length=50, default='Times New Roman')
    fontSize = models.CharField(max_length=10, default='16px')
    parMargin = models.CharField(max_length=10, default='1em')
    lineHeight = models.CharField(max_length=10, default='normal')


class Library(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    articles = models.ManyToManyField(
        'Article', related_name='libraries')


class Article(models.Model):
    url = models.URLField(primary_key=True)
    title = models.CharField(max_length=100)
    # TODO: @alex - revisit this - what will be the format of the content?Parser?
    # content = models.FileField()


class ArticleNotes(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()


class Session(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    startTime = models.DateTimeField(auto_now_add=True)
    endTime = models.DateTimeField(auto_now=True)


class Selection(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    selectionNote = models.OneToOneField(
        'SelectionNotes', on_delete=models.CASCADE)
    paragraphIndex = models.IntegerField()
    startWordIndex = models.IntegerField()
    endWordIndex = models.IntegerField()


class SelectionNotes(models.Model):
    highlight = models.ForeignKey(Selection, on_delete=models.CASCADE)
    content = models.TextField()
