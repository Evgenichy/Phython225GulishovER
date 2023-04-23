from django.contrib import admin
from .models import Cards, Size, Order


class CardsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('card_name',)}


admin.site.register(Cards, CardsAdmin)
admin.site.register(Size)
admin.site.register(Order)

