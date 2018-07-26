from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
	path('', landing, name='landing'),
	path('listsearch/', listsearch, name='listsearch'),
	path('search/', searchcontext, name='searchcontext'),
]