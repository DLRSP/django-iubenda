from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Iubenda


@admin.register(Iubenda)
class IubendaAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ["site", "iub_site_id", "iub_policy_id"]
    list_display_links = ["site"]
    ordering = ["site", "iub_site_id", "iub_policy_id"]
    search_fields = ["site"]
