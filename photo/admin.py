from django.contrib import admin

# Register your models here.
from photo.models import *


class ImageInline(admin.TabularInline):
    model = Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'album', 'is_public']
    ordering = ['album']
    readonly_fields = ['image_tag']
    list_filter = ('album', 'is_public')


class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    list_display = ['name', 'is_public']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['image_tag']


class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_public']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['image_tag']


class MediaAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_public']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['image_tag']


admin.site.register(Album, AlbumAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Media, MediaAdmin)

# def save_model(self, request, obj, form, change, **kwargs):
#     obj.save()
#     for afile in request.FILES.getlist('photos_multiple'):
#         obj.image = afile.url
#         obj.save()
