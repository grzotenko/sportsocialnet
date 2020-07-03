from django.conf.urls import url, include
from django.urls import path, re_path

from .controllers import MainPage

urlpatterns = [
    path('', MainPage.as_view(), name="main_main"),
    # url(r'^', MainPage.as_view(), name="main_main"),
]