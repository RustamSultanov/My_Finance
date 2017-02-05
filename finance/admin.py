from django.contrib import admin
from finance.models import User, Account, Charge
# Register your models here.

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Charge)