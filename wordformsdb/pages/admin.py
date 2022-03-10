from django.contrib import admin

from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    search_fields = ('wordform',)
    list_filter = ('wordform',)

admin.site.register(Entry, EntryAdmin)
