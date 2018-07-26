from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import (
        authenticate,
        get_user_model,
        login,
        logout,
    )
from django.db.models import Q

from .models import *

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
import json
import urllib

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.views.generic import RedirectView

from django.contrib.sessions.models import Session
from django.utils import timezone
from videoblog.models import *

def landing(request):
	videoblog = VideoBlog.objects.all().order_by("-data")[:5]
	context = {
        "title": "HOME",
		"videoblog": videoblog,
	}
	return render(request, 'home/content.html', context)


def listsearch(request):
    listsearch = VideoBlog.objects.all()

    search = request.GET.get("q")
    if search:
        listsearch = listsearch.filter(
            Q(title__icontains=search)|
            Q(opisaniye__icontains=search)
            ).distinct()

    context = {
            "listsearch": listsearch,
        }
    return render(request, 'home/listsearch.html', context)


def searchcontext(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    listsearch = VideoBlog.objects.filter(title__icontains=search_text)
    context = {
        "listsearch":listsearch,
    }
    return render(request, 'home/allsearch.html',context)