from django.contrib import admin
from order_table.models import User, Order, Port, Customer

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Port)
admin.site.register(Customer)

# Register your models here.
