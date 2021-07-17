from django.contrib import admin
from .models import BossTable, CustomerQuery

# Register your models here.

admin.site.register(BossTable)
admin.site.register(CustomerQuery)
