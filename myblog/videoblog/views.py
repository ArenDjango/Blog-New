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
from .models import *
from accounts.models import UserProfile

from ipware import get_client_ip

def videohome(request):
	return render(request, 'videoblog/contentvideo.html')

def videodetail(request, id=None):
	user = request.user
	video = VideoBlog.objects.get(id=id)
	videoblog = VideoBlog.objects.all().order_by("-data")[:4]
	title = video.title
	if user.is_authenticated:
		if video not in user.userprofile.story.all():
			user.userprofile.story.add(video)
	context = {
		"title": title,
		"video":video,
		"videoblog":videoblog,
	}
	# ipobject = IpAdress.objects.all()
	#ip = request.POST['ip_adress']
	# ip = get_client_ip(request)
	# x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	# if x_forwarded_for:
	# 	ip = x_forwarded_for.split(',')[0]
	# else:
	# 	ip = request.META.get('REMOTE_ADDR')
	# ipok = IpAdress.objects.create(ip_adress=ip)
	# print('*********************')
	# finish = '{}'.format(ipok.ip_adress)
	# print(ip)
	# print('*********************')
	# if finish not in video.views.all():
	#	video.views.add(finish)
	return render(request, 'videoblog/videodetail.html', context)

def videoview(request, id=None):
	video = VideoBlog.objects.get(id=id)
	user = request.user

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def videoedit(request, id=None):
	video = VideoBlog.objects.get(id=id)
	user = request.user
	if video.user == request.user and request.method == 'POST':
		print('***********************')
		video.title = request.POST.get('title')
		video.opisaniye = request.POST.get('opisaniye')
		video.imgtitle = request.FILES['image']
		video.video = request.FILES['video']
		print(video.title)
		video.save()
		print('Ok')
		print('***********************34553345')
	context = {
		"video": video,
		"user": user,
	}
	return render(request, 'videoblog/editvideo.html', context)

