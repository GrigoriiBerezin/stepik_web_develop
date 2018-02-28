# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return self.on_order('-added_at')
    def popular(self):
        return self.on_order('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True)

    author = models.ForeignKey(User,
	   null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, 
         related_name='likes_set')    
    object = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User,
	   null=True, on_delete=models.SET_NULL)
    question = models.ForeignKey(Question, 
             null=True, on_delete=models.SET_NULL)
