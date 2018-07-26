from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from markdown_deux import markdown

from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User


class IpAdress(models.Model):
	ip_adress = models.GenericIPAddressField(default='192.168.0.1')
	def __unicode__(self):
		return self.ip_adress

class VideoBlog(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
								on_delete=models.CASCADE)
	title = models.TextField()
	data = models.DateTimeField(auto_now=True, 
						auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	imgtitle = models.ImageField(upload_to='imgvideos')
	video = models.FileField(upload_to='videos')
	opisaniye = models.TextField()
	videotype = models.TextField(null=False)

	# likes = 
	views = models.ManyToManyField(IpAdress)
	# comments = 
	def __unicode__(self):
		return self.title

