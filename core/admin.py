from django.contrib import admin

from .models import TeamMember, ProsoftDoc, MarketRate

# Register your models here
@admin.register(ProsoftDoc)
class ProsoftDocAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'slug')


# Register your models here.
admin.site.register(TeamMember)
admin.site.register(MarketRate)
