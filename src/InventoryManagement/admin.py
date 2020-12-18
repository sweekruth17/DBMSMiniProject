from django.contrib import admin

# Register your models here.

from .models import Supplier,Order,Product,Category,Sell,Stock

class SupplierCreateAdmin(admin.ModelAdmin):
    list_display = ['supplier_name', 'enterprise_name', 'mobile_number', 'email_id']

class OrderCreateAdmin(admin.ModelAdmin):
    list_display = ('date_ordered','number_ordered')

    def get_supplier_name(self, obj):
        return obj.Supplier.supplier_name
    get_supplier_name.admin_order_field = 'supplier__name'


admin.site.register(Supplier, SupplierCreateAdmin)
admin.site.register(Order, OrderCreateAdmin)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Sell)
admin.site.register(Stock)

#lol this is a test
#en guru work e aaitilla