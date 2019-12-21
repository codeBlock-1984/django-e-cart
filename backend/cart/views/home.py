from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import views
from rest_framework.decorators import api_view
from ..models import User, Product, Category, Order, Item


# Create your views here.
def index(request):
    res = 'Welcome to E-Cart!'
    return HttpResponse(res)
