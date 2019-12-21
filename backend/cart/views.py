import logging
import json
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import views
from rest_framework.decorators import api_view
from .models import User, Product, Category, Order, Item
from .validate import generate, validate

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

# Create your views here.
@csrf_exempt
@api_view(['GET'])
def index(request):
    res = 'Welcome to E-Cart!'
    return HttpResponse(res)

@api_view(['POST'])
def login(request):
    username_input = request.data['username']
    password_input = request.data['password']
    #logger.info(username_input)

    try:
        user = User.objects.get(username=username_input, password=password_input)
        user_token = generate({'name': username_input})
        return HttpResponse(user_token, status=200)

    except Exception as error:
        #print(error)
        return HttpResponse('Incorrect login details!', status=400)

@api_view(['POST']) 
def place_order(request, *args):
    data = json.loads(request.body)

    try:
        token = request.headers['token']
        is_permitted = validate(token)

    except:
        return HttpResponse('User not authenticated!', status=401)

    if not is_permitted:
        return HttpResponse('User not authenticated!', status=401)

    customer = get_object_or_404(User, pk=data['customer'])
    order_list = data['order']

    for item in order_list:
        order_item_input = get_object_or_404(Product, pk=item['product'])
        quantity_input = item['quantity']
        new_order = Order(customer=customer)
        new_order.save()
        new_order_item = Item(
            order=new_order,
            order_item=order_item_input,
            quantity=quantity_input
        )
        new_order_item.save()
    return HttpResponse('Order successful', status=201)

