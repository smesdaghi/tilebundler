from django.contrib import admin
from tilebundler.models import Tileset

class TilesetAdmin(admin.ModelAdmin):
    fields = ['name', 'created_by']
    list_display = ('name', 'created_by', 'created_at')
    search_fields = ['name']

admin.site.register(Tileset, TilesetAdmin)