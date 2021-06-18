from django.contrib import admin

from .models import ConstitucionalAct, TeamMember, ProsoftDoc, Description

# Register your models here
@admin.register(ProsoftDoc)
class ProsoftDocAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'slug')


@admin.register(ConstitucionalAct)
class ConstitucionalActAdmin( admin.ModelAdmin):
    readonly_fields = ('updated',)


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    readonly_fields = ('updated',)

# Register your models here.
admin.site.register(TeamMember)
