from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import (
		authenticate,
		get_user_model,
		login,
		logout,
	)
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, User
from django.db.models import Q


from django.conf import settings
from django.contrib import messages

import json
import urllib
from videoblog.models import *
from .models import UserProfile

from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.views.generic import RedirectView

from django.contrib.sessions.models import Session
from django.utils import timezone


def loginuser(request):
	username = request.POST['login']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('/')
	else:
		return redirect('/sadasda/')
	return render(request, 'home/home.html')

def loginoutuser(request):
	logout(request)
	return redirect('/')

def registeruser(request):
	login = request.POST.get('username', None)
	mail = request.POST.get('mail', None)

	firstname = request.POST.get('firstname', None)
	lastname = request.POST.get('lastname', None)

	password = request.POST.get('password', None)
	passwordtwo = request.POST.get('passwordtwo', None)

	user = User.objects.create_user(username=login, password=password)
	user.first_name = firstname
	user.last_name = lastname
	user.email = mail
	user.save()
	# loginin = authenticate(request, username=login, password=password)
	# login(request, loginin)
	return redirect('/')
	
def kabinet(request):
	profilemy = UserProfile.objects.get_or_create(user=request.user)
	user = request.user
	pofile = UserProfile.objects.all()
	videoblog = VideoBlog.objects.all().order_by("-updated")
	context = {
		"user": user,
		"userpofile": pofile,
		"title": "PROFILE",
		"videoblog": videoblog,
	}
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		user.userprofile.avatar = myfile
		user.userprofile.save()
	return render(request, 'accounts/kabinet.html', context)


def kabinetstory(request):
	user = request.user
	pofile = UserProfile.objects.all()
	videoblog = VideoBlog.objects.all().order_by("-updated")
	context = {
		"user": user,
		"userpofile": pofile,
		"title": "PROFILE",
		"videoblog": videoblog,
	}
	return render(request, 'accounts/kabinetstory.html', context)	

def addvideo(request):
	if request.method == "POST":
		title = request.POST.get('title')
		opisaniye = request.POST.get('opisaniye')
		img = request.POST.FILES['image']
		video = request.POST.FILES['video']
		user = request.user.get_full_name
		VideoBlog.objects.create(
			user=request.user, 
			title=title,
			imgtitle=img,
			opisaniye=opisaniye,
			video=video,
			videotype='video'
			)
	# return JsonResponse({'title': title, 'opisaniye': opisaniye, 'img':img, 'video':video, 'user':user})
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))