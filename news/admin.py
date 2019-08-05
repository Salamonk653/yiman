from django.contrib import admin

# Register your models here.
from news.models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class SliderAdmin(admin.ModelAdmin):
    list_filter = ('language',)
    list_display = ['image_tag', 'fon', 'language']
    readonly_fields = ['image_tag']

class NewAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'category', 'likes', 'dislikes', 'is_public']
    ordering = ['category']
    readonly_fields = ['image_tag']
    search_fields = ('name', 'text')
    list_filter = ('category', 'is_public', 'language')
    list_per_page = 20
    # list_display_links = 'name'


admin.site.register(Kairymduuluk)
admin.site.register(OFonde)
admin.site.register(Fon)
admin.site.register(Slider, SliderAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(Fondjonundo)
