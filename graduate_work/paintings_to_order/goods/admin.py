from django.contrib import admin
from .models import Cards, Size, Price, Order


class CardsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('card_name',)}


admin.site.register(Cards, CardsAdmin)
admin.site.register(Size)
admin.site.register(Price)
admin.site.register(Order)

