from django.contrib import admin

from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    list_filter = ['published_date']
    search_fields = ['title']
    date_heirarchy = 'published_date'
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
