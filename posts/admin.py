from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'url',
        'number_of_votes'
    )

    search_fields = [
        'title'
    ]
