from django.contrib import admin
from .models import Payment, User


class UserAdmin(admin.ModelAdmin):
    user = User()
    list_display = user.get_field_names()


class PaymentAdmin(admin.ModelAdmin):
    list_payments = ["id", "user", "date", "sum", "comment"]


admin.site.register(Payment, PaymentAdmin)
admin.site.register(User, UserAdmin)
