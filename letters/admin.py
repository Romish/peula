from django.contrib import admin
from letters.models import Organization, Letter

class OrganizationAdmin(admin.ModelAdmin):
    pass


class LetterAdmin(admin.ModelAdmin):
    search_fields = ["subject", "content"]
    list_display = ["author", "organization", "subject"]
    list_filter = ["organization"]




admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Letter, LetterAdmin)
