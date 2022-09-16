from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('buy/<int:item_id>', buy, name='buy'),
    path('items', items, name='items'),
    path('item/<int:item_id>', item, name='item'),
    path('add_test_items', add_test_items),
    path('success_buy', success, name="success"),
    path('cancel_buy', cancel, name="cancel"),
]
