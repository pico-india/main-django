from django.contrib import admin
from .models import Image, Category
class ImageAdmin(admin.ModelAdmin):
    list_display = ('date', 'image', 'tags', 'category', 'user')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Image, ImageAdmin)
admin.site.register(Category, CategoryAdmin)
