# -*- coding: utf-8 -*-
# Create your models here.
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from sorl.thumbnail import ImageField

from news.models import Language


class Album(models.Model):
    class Meta:
        verbose_name = u'Альбом'
        verbose_name_plural = u'Альбомдор'
        ordering = ['-created']

    name = models.CharField(verbose_name=u'Альбомдун аты', max_length=250, db_index=True)
    ru_name = models.CharField(verbose_name=u'Орусча аты', max_length=250, db_index=True)
    oblojka = models.ImageField(verbose_name=u'Альбомдун обложкасы', upload_to='album/oblojka/')
    slug = models.CharField(verbose_name=u'Транслит', max_length=200, blank=True)
    is_public = models.BooleanField(verbose_name=u'Көрүнсүн', default=True)
    created = models.DateTimeField(verbose_name=u'Дата', default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.oblojka.url))

    image_tag.short_description = 'Сүрөт'

    def delete(self, *args, **kwargs):
        self.oblojka.delete(save=False)
        super(Album, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('album_detail', kwargs={'slug': self.slug})


class Image(models.Model):
    class Meta:
        verbose_name = u'Сүрөт'
        verbose_name_plural = u'Сүрөттөр'
        ordering = ['-id']

    album = models.ForeignKey(Album, verbose_name=u'Албом', on_delete=models.CASCADE, blank=True, null=True,
                              default=None)
    image = ImageField(verbose_name=u'Сүрөт', upload_to='gallery/')
    description = models.TextField(verbose_name=u'Маалымат', blank=True, null=True)
    ru_description = models.TextField(verbose_name=u'Орусча', blank=True, null=True)
    is_public = models.BooleanField(verbose_name=u'Көрүнсүн', default=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

    image_tag.short_description = 'Сүрөт'

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(Image, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('photo_detail', kwargs={'id': self.id})


class Video(models.Model):
    class Meta:
        verbose_name = u'Видео'
        verbose_name_plural = u'Видеолор'
        ordering = ['-id']

    language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Видеонун аты', max_length=250, db_index=True)
    ru_name = models.CharField(verbose_name=u'Орусча аты', max_length=250, db_index=True)
    oblojka = models.ImageField(verbose_name=u'Видеонун обдожкасы', upload_to='video/')
    slug = models.CharField(verbose_name=u'Транслит', max_length=200, blank=True)
    video_url = models.CharField(verbose_name=u'Видеонун ссылкасы', max_length=200, blank=True)
    is_public = models.BooleanField(verbose_name=u'Көрүнсүн', default=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.oblojka.url))

    image_tag.short_description = 'Сүрөт'

    def __str__(self):
        return self.name


class Media(models.Model):
    class Meta:
        verbose_name = u'Долбоор'
        verbose_name_plural = u'Долбоорлор'
        ordering = ['-id']

    language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Долбоордун аты', max_length=250, db_index=True)
    oblojka = models.ImageField(verbose_name=u'Долбоордун обдожкасы', upload_to='video/')
    slug = models.CharField(verbose_name=u'Транслит', max_length=200, blank=True)
    dolboor_url = models.FileField(verbose_name=u'Долбоордун ссылкасы', upload_to='files/',  max_length=200, blank=True)
    is_public = models.BooleanField(verbose_name=u'Көрүнсүн', default=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.oblojka.url))

    image_tag.short_description = 'Сүрөт'

    def __str__(self):
        return self.name