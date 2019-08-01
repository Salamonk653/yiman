from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from sorl.thumbnail import ImageField


class Album(models.Model):
    class Meta:
        verbose_name = u'Альбом'
        verbose_name_plural = u'Альбомдор'
        ordering = ['-created']

    name = models.CharField(verbose_name=u'Альбомдун аты', max_length=250, db_index=True)
    slug = models.CharField(verbose_name=u'Транслит', max_length=200, blank=True)
    is_public = models.BooleanField(verbose_name=u'Көрүнсүн', default=True)
    created = models.DateTimeField(verbose_name=u'Дата', default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.name

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
    is_public = models.BooleanField(verbose_name=u'Көрүнсүн', default=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

    image_tag.short_description = 'Сүрөт'

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(Image, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('photo_detail', kwargs={'id': self.id})