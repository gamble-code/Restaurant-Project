from django.contrib import admin


from .models import Menu
from .models import Booking


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=['name', 'price', 'menu_item_description']

@admin.register(Booking)
class MenuAdmin(admin.ModelAdmin):
    list_display=['first_name', 'reservation_date', 'reservation_slot']