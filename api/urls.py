from django.conf.urls import url, include
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title="FOOTBALL API")

from .views import api_root
from main.views import TestView
urlpatterns = [
    url(r'^root/$', api_root),
    url(r'^$', schema_view),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('test/', TestView.as_view(), name='test-test'),

]