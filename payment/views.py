from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import stripe
from .models import Item
from djsite.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY


def index(request):
    return redirect(items)


def cancel(request):
    return render(request, 'payment/cancel.html')


def success(request):
    session_id = request.GET["session_id"]
    session = stripe.checkout.Session.retrieve(session_id)
    customer = session["customer_details"]["name"]
    context = {"customer": customer}
    return render(request, 'payment/success.html', context)


# Create your views here.
def item(request, item_id):
    if request.method == "GET":
        item = get_object_or_404(Item, pk=item_id)
        title = f"Buy item {item.pk}"
        context = {'item': item, 'title': title, "public_key": STRIPE_PUBLIC_KEY}
        return render(request, 'payment/item.html', context)


def buy(request, item_id):
    if request.method == "GET":
        item = Item.objects.get(pk=item_id)
        product = stripe.Product.create(name=item.name)
        price = stripe.Price.create(
            product=product, unit_amount=item.price, currency=item.currency
        )
        try:
            session = stripe.checkout.Session.create(
                line_items=[{"price": price, "quantity": 1}],
                mode='payment',
                success_url='http://localhost:8000/success/',
                cancel_url='http://localhost:8000/cancel/',
            )
        except Exception as e:
            print(e)
            return str(e)

        return JsonResponse({"session_id": session['id']})


def add_test_items(request):
    if Item.objects.count() == 0:
        Item.objects.create(
            name='Bread',
            description='Bread is a staple food prepared from a dough of flour and water, usually by baking.',
            price=22000,
            currency='RUB'
        )
        Item.objects.create(
            name='Carrot',
            description='The carrot is a root vegetable, typically orange in color.',
            price=100000,
            currency='RUB'
        )
        Item.objects.create(
            name='Apple',
            description='An apple is an edible fruit produced by an apple tree.',
            price=50000,
            currency='RUB'
        )
        Item.objects.create(
            name='Banana',
            description='A banana is an elongated, edible fruit – botanically a berry',
            price=160000,
            currency='RUB'
        )
        return HttpResponse('Данные внесены')
    return HttpResponse('Данные уже внесены')


def items(request):
    if request.method == "GET":
        items = Item.objects.all()
        context = {'items': items, 'title': 'Items'}
        return render(request, 'payment/items.html', context)
