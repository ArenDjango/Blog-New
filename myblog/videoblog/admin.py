from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *



# class Ip(admin.ModelAdmin):
# 	class Meta:
# 		model = IpAdress

class Video(admin.ModelAdmin):
	list_display = ["id","title", "data"]
	list_display_links = ["title"]
	list_filter = ["data"]
	search_fields = ["title"]
	fields = ["user", "title", 
	"imgtitle", "video", "opisaniye", "views"
	]
	class Meta:
		model = VideoBlog

admin.site.register(VideoBlog, Video)
admin.site.register(IpAdress)