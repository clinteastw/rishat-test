from typing import Optional
import stripe

from django.urls import reverse
from project.settings import STRIPE_SECRET_KEY
from .models import Item, Order

stripe.api_key = STRIPE_SECRET_KEY

def create_stripe_checkout_session(request, item: Optional[Item] = None, order: Optional[Order] = None):
    if order:
        line_items = []
        for item in order.items.all():
            line_items.append({
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            })
            
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            discounts=[{
                'coupon': order.discount.stripe_coupon_id,
            }] if order.discount else None,
            success_url=request.build_absolute_uri(reverse('success')),
            cancel_url=request.build_absolute_uri(reverse('cancel')),
            automatic_tax={'enabled': True},
        )
        return session  
         
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success')),
        cancel_url=request.build_absolute_uri(reverse('cancel')),
        automatic_tax={'enabled': True},
    )
    return session