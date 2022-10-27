from django.contrib import admin
from video.models import Video
class Videos(admin.ModelAdmin):
    list_display=("id","titulo","descricao")
    list_display_links=("id","titulo")
    search_fields=("titulo",)

admin.site.register(Video,Videos)
