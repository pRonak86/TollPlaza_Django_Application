from django.contrib import admin

# Register your models here.
from Toll.models import Customer_Registration, Ewallet, Employee, FinalAmount

admin.site.register(Customer_Registration)
admin.site.register(Ewallet)
admin.site.register(Employee)
admin.site.register(FinalAmount)
