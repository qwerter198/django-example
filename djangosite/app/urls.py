from django.urls import re_path
from . import views

# 應用程式的URL 需要incloud到djangosite.urls.py

urlpatterns = [
    re_path(r'moments_input', views.moments_input),
    re_path(r'', views.welcome, name='first-url')
]
