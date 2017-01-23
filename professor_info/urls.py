from django.conf.urls import url

from professor_info.views import *

urlpatterns = [
    url(r'^', index),
]
