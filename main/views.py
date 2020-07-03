from django.shortcuts import render
from django.views import View
from rest_framework import views
from rest_framework.response import Response
from datetime import date, timedelta

class TestView(views.APIView):
    def get(self, request):
        return Response([
            {"lol": "kek", "id": "0"},
            {"losadl": "keqdwk", "id": "1"},
        ])
