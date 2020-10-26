from django.contrib import admin
from typing import Any

from .models import Unity, UnityContent
from core.models import TeamMember


# Register your models here.
class UnityAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', )


class UnityContentAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'slug')

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        user = TeamMember.objects.get(user=request.user)
        obj.created_by = user
        obj.save()

admin.site.register(Unity, UnityAdmin)
admin.site.register(UnityContent, UnityContentAdmin)
