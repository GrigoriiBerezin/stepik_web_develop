# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')


#class QuestionManager(models.Manager):
#    def main(self, since, limit=10):
#        qs = self.order_by('-id')
#        res = []
#        if since is not None:
#            qs = qs.filter('id__lt'=since)
#        for p in qs[:1000]:
#            if len(res) == 0:
#                res.append(p)
#            elif res[-1].category != p.category:
#                res.append(p)
#            if len(res) >= limit:
#                break
#        return res


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True)

    author = models.ForeignKey(User,
                               null=True,
                               on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User,
                                   related_name='likes_set')
    objects = QuestionManager()

    def get_url(self):
        return "/question/{}/".format(self.id)

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User,
                               null=True,
                               on_delete=models.SET_NULL)
    question = models.ForeignKey(Question,
                                 null=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.text
 
