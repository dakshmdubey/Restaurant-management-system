from django.contrib import admin
from .models import MenuItem, Order,Table

admin.site.register(MenuItem)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'food_item', 'quantity', 'status','order_date','get_total_price')
    list_editable = ('status',)

    def get_total_price(self, obj):
        return obj.quantity * obj.food_item.price

    get_total_price.short_description = "Total Price"
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'status')