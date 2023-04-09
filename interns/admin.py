from django.contrib import admin
from .models import Payment


class UserAdmin(admin.ModelAdmin):
    list_display = ["user_name"]


class PaymentAdmin(admin.ModelAdmin):
    list_payments = ["id", "date", "sum", "comment"]

admin.site.register(Payment, PaymentAdmin)

