from django.contrib import admin

from .models import Unity, UnityContent


# Register your models here.
class UnityAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', )


class UnityContentAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'slug')


admin.site.register(Unity, UnityAdmin)
admin.site.register(UnityContent, UnityContentAdmin)
