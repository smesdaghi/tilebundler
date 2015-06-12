from django.contrib import admin
from models import Tileset

class TilesetAdmin(admin.ModelAdmin):
    fields = ['name', 'created_by', 'server_url', 'server_service_type', 'server_username', 'server_password', 'layer_name', 'layer_zoom_start', 'layer_zoom_stop', 'geom']

    list_display = ('name', 'layer_name', 'server_url', 'created_by', 'created_at')
    search_fields = ['name']

admin.site.register(Tileset, TilesetAdmin)