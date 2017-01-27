from django.conf.urls import url

from professor_info.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^search_query/$', search_query),

]
