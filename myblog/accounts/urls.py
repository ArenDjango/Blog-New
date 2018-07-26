from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
	path('kabinet/', kabinet, name='kabinet'),
	path('kabinet/tab=story/', kabinetstory, name='kabinetstory'),
	path('kabinet/addvideo/', addvideo, name='addvideo'),
]