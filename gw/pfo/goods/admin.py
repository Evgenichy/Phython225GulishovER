from django.contrib import admin
from .models import Goods, Size, Order, ComForm


class GoodsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('card_name',)}


admin.site.register(Goods)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(ComForm)
