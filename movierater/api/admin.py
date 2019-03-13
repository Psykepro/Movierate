from django.contrib import admin
from movierater.api.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('title', 'description')
    list_display = ['title', 'description']
    search_fields = ('title', 'description')
