from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'currency',
    )

    def price(self, obj: Item):
        return obj.get_price_show()


admin.site.register(Item, ItemAdmin)
