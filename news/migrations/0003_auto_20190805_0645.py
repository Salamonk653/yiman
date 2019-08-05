# Generated by Django 2.2.1 on 2019-08-05 00:45

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190805_0408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ofonde',
            name='text',
        ),
        migrations.AddField(
            model_name='ofonde',
            name='bagyt',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Багыттар'),
        ),
        migrations.AddField(
            model_name='ofonde',
            name='baikoochu',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Байкоочу кеңеш'),
        ),
        migrations.AddField(
            model_name='ofonde',
            name='ish',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Иш чаралар'),
        ),
        migrations.AddField(
            model_name='ofonde',
            name='maksat',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Максаты'),
        ),
        migrations.AddField(
            model_name='ofonde',
            name='otchet',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Отчет'),
        ),
    ]