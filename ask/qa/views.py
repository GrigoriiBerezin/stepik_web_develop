# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, Http404
from django.core.paginator import Paginator, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from .models import Question


# Create your views here.
def question_page(request, num):
    try:
        question = Question.objects.get(id=num)
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'question.html',
                  {'question': question})


def index(request):
    qs = Question.objects.all()
    page = paginate(request, qs)
    return render(request, 'index.html',
                  {'page': page})


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page
