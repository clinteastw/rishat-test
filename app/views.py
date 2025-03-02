from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from project.settings import STRIPE_PUBLIC_KEY
from .models import Item, Order
from .services import create_stripe_checkout_session


def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})


def get_item(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'item.html', {'item': item, 'STRIPE_PUBLIC_KEY': STRIPE_PUBLIC_KEY})


def buy_item(request, id):
    item = get_object_or_404(Item, id=id)
    session = create_stripe_checkout_session(request, item=item)
    return JsonResponse({'session_id': session.id})


def get_order(request, id):
    order = get_object_or_404(Order, id=id)
    order.calculate_total_price()
    return render(request, 'order.html', {'order': order, 'STRIPE_PUBLIC_KEY': STRIPE_PUBLIC_KEY})

def buy_order(request, id):
    order = get_object_or_404(Order, id=id)
    session = create_stripe_checkout_session(request, order=order)
    return JsonResponse({'session_id': session.id})

def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')