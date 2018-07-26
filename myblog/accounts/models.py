from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from markdown_deux import markdown

from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User
from videoblog.models import VideoBlog
User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, 
                on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='imageusers', 
                null=True,
                verbose_name='Изображение')

    followers = models.ManyToManyField(User, 
                related_name='is_following',
                blank=True)
    following = models.ManyToManyField(User,
              related_name='is_followers',
              blank=True)

    story = models.ManyToManyField(VideoBlog,
                related_name='story',
                blank=True)
    view_later = models.ManyToManyField(VideoBlog, 
                    related_name='view_latter',
                    blank=True)
    story_false = models.BooleanField(default=True)


    def __unicode__(self):
        return self.user




class Meta:
    verbose_name = 'Профиль'
