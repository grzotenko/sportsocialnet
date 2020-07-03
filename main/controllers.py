from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse

from .models import *
from .views import TestView

class MainPage(View):
    initial = {'key': 'value'}
    template_name = 'index.html'

    def get(self, request):  # , *args, **kwargs):
        context = dict()
        return render(request, self.template_name, context)

