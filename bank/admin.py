from bank.models import Customer, trans_details
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(trans_details)