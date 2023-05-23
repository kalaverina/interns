from django.contrib import admin
from .models import Payment, User, Tag

class TagsAdmin(admin.ModelAdmin):
    tag = Tag()
    fields = ['name']

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','tag_list']
    list_filter = ['name']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


   # user = User()
    #tag_list = user.tags.all()
    #list_display = user.get_field_names()
    #fields = user.get_field_names()

class PaymentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "date", "sum", "comment"]


admin.site.register(Payment, PaymentAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagsAdmin)