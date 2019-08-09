# -*- coding: utf-8 -*-
# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe


class Language(models.Model):
    class Meta:
        db_table = u'Тил'
        verbose_name = u'Тил'
        verbose_name_plural = u'Тилдер'
        ordering = ['-id']

    name = models.CharField(verbose_name=u'Аты', max_length=80, blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        db_table = u'Category'
        verbose_name = u'Категория'
        verbose_name_plural = u'Категориялар'
        ordering = ['-id']

    name = models.CharField(verbose_name=u'Аты', max_length=80, blank=True, null=True, default=None)
    slug = models.CharField(verbose_name=u'Транслит', max_length=200, blank=True)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class New(models.Model):
    class Meta:
        verbose_name_plural = u'Жаңылыктар'
        verbose_name = u'Жаңылык'
        ordering = ['-id']

    category = models.ForeignKey(Category, verbose_name=u'Категория',
                                 default=1, on_delete=models.CASCADE,
                                 blank=True, null=True)
    language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Макаланын аталышы', db_index=True, max_length=255)
    slug = models.CharField(verbose_name=u'Транслит', max_length=200, blank=True)
    image = models.ImageField(verbose_name=u'Сүрөт', upload_to='news/', blank=True, null=True)
    text = RichTextUploadingField(verbose_name=u'Маалымат')
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    user_rection = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    created = models.DateTimeField(verbose_name=u'Дата', default=timezone.now)
    author = models.CharField(verbose_name=u'Макаланын автору', blank=True, null=True, max_length=200)
    is_public = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

    image_tag.short_description = 'Сүрөт'

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(New, self).delete(*args, **kwargs)


class Kairymduuluk(models.Model):
    class Meta:
        verbose_name_plural = u'Кайрымдуулук'
        verbose_name = u'Кайрымдуулук'
        ordering = ['-id']

    language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
    bilim_aluu = models.IntegerField(verbose_name=u'Билим алууга', default=0)
    kurbandyk = models.IntegerField(verbose_name=u'Курбандыкка', default=0)
    muktaj = models.IntegerField(verbose_name=u'Муктаждарга', default=0)
    suu_chygaruu = models.IntegerField(verbose_name=u'Суу чыгарууга', default=0)
    text = RichTextUploadingField(verbose_name=u'Маалымат')

    def __str__(self):
        return str(self.id)


class Fon(models.Model):
    class Meta:
        verbose_name_plural = u'Фоны'
        verbose_name = u'Фон'
        ordering = ['-id']

    logo = models.ImageField(verbose_name=u'Лого', upload_to='ofonde/')
    ofonde_fon = models.ImageField(verbose_name=u'фонд', upload_to='slider/')
    video = models.ImageField(verbose_name=u'Видео', upload_to='ofonde/')
    foto = models.ImageField(verbose_name=u'Фотогаларея', upload_to='ofonde/')
    media = models.ImageField(verbose_name=u'Медиа', upload_to='ofonde/')

    def __str__(self):
        return str(self.id)


class OFonde(models.Model):
    class Meta:
        verbose_name_plural = u'Фонд жөнүндө'
        verbose_name = u'Фонд жөнүндө'
        ordering = ['-id']

    name = models.CharField(verbose_name=u'Аты', max_length=250)
    phone = models.CharField(verbose_name=u'Телефон', max_length=150, db_index=True)
    email = models.EmailField(verbose_name=u'Емейл')
    adres = models.CharField(verbose_name=u'Дарек', max_length=200, db_index=True)
    karta = models.CharField(verbose_name=u'Карта', max_length=400)
    facebook = models.CharField(verbose_name=u'Фейсбук', max_length=250, blank=True, null=True)
    instagram = models.CharField(verbose_name=u'Инстаграм', max_length=250, blank=True, null=True)
    youtube = models.CharField(verbose_name=u'Ютуб', max_length=250, blank=True, null=True)
    language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Slider(models.Model):
    class Meta:
        db_table = u'Слайдер'
        verbose_name_plural = u'Слайдеры'
        verbose_name = u'Слайдер'
        ordering = ['-id']

    language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
    fon = models.ImageField(verbose_name=u'Слайдердин сүрөтү', upload_to='slider/')

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.fon.url))

    image_tag.short_description = 'Сүрөт'


class Fondjonundo(models.Model):
    class Meta:
        db_table = u'Фонд'
        verbose_name_plural = u'Фонддун ачыктамасы'
        verbose_name = u'Фонддун ачыктамасы'
        ordering = ['-id']

    language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Аты', max_length=100)
    text = RichTextUploadingField(verbose_name=u'Багыттар', blank=True, null=True)

    def __str__(self):
        return self.name
