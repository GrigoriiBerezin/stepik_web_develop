# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponce

def test(request, *args, **kwargs):
    return HttpResponce('OK')
