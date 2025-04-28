from django.contrib import admin
from .models import Post


# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner__username",  "created_at", "updated_at", "cover")
    list_filter = ("created_at", "owner__username")
    search_fields = ("id", "title", "description")
    readonly_fields = ('views_count',)