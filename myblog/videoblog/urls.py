from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
	path('', videohome, name='videohome'),
	path('<int:id>/', videodetail, name='videodetail'),
	path('<int:id>/view/', videoview, name='videoview'),
	path('<int:id>/edit/', videoedit, name='videoedit'),
]