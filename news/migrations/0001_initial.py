# Generated by Django 2.2.1 on 2019-07-31 20:06

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=80, null=True, verbose_name='Аты')),
                ('slug', models.CharField(blank=True, max_length=200, verbose_name='Транслит')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категориялар',
                'db_table': 'Category',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=80, null=True, verbose_name='Аты')),
            ],
            options={
                'verbose_name': 'Тил',
                'verbose_name_plural': 'Тилдер',
                'db_table': 'Тил',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_fon', models.ImageField(upload_to='slider/', verbose_name='Слайдер фон')),
                ('ofonde_fon', models.ImageField(upload_to='slider/', verbose_name='фон фонда')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдер',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='OFonde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='ofonde/', verbose_name='Лого')),
                ('video', models.ImageField(upload_to='ofonde/', verbose_name='Видео')),
                ('foto', models.ImageField(upload_to='ofonde/', verbose_name='Фотогаларея')),
                ('media', models.ImageField(upload_to='ofonde/', verbose_name='Медиа')),
                ('name', models.CharField(max_length=250, verbose_name='Аты')),
                ('phone', models.CharField(db_index=True, max_length=150, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Емейл')),
                ('adres', models.CharField(db_index=True, max_length=200, verbose_name='Даарек')),
                ('karta', models.CharField(max_length=400, verbose_name='Карта')),
                ('facebook', models.CharField(blank=True, max_length=250, null=True, verbose_name='Фейсбук')),
                ('instagram', models.CharField(blank=True, max_length=250, null=True, verbose_name='Инстаграм')),
                ('youtube', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ютуб')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Маалымат')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Language', verbose_name='Тили')),
            ],
            options={
                'verbose_name': 'Фонд жөнүндө',
                'verbose_name_plural': 'Фонд жөнүндө',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Макаланын аталышы')),
                ('slug', models.CharField(blank=True, max_length=200, verbose_name='Транслит')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news/', verbose_name='Сүрөт')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Маалымат')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('author', models.CharField(blank=True, max_length=200, null=True, verbose_name='Макаланын автору')),
                ('is_public', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Category', verbose_name='Категория')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Language', verbose_name='Тили')),
                ('user_rection', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Макала',
                'verbose_name_plural': 'Макалалар',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Kairymduuluk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Маалымат')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Language', verbose_name='Тили')),
            ],
            options={
                'verbose_name': 'Кайрымдуулук',
                'verbose_name_plural': 'Кайрымдуулук',
                'ordering': ['-id'],
            },
        ),
    ]
