# Generated by Django 2.2.1 on 2019-08-01 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190801_0602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_fon', models.ImageField(upload_to='slider/', verbose_name='Слайдер')),
                ('ofonde_fon', models.ImageField(upload_to='slider/', verbose_name='фонд')),
                ('video', models.ImageField(upload_to='ofonde/', verbose_name='Видео')),
                ('foto', models.ImageField(upload_to='ofonde/', verbose_name='Фотогаларея')),
                ('media', models.ImageField(upload_to='ofonde/', verbose_name='Медиа')),
                ('kairymduuluk', models.ImageField(upload_to='ofonde/', verbose_name='Кайрымдуулук')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдер',
                'ordering': ['-id'],
            },
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
        migrations.RemoveField(
            model_name='ofonde',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='ofonde',
            name='media',
        ),
        migrations.RemoveField(
            model_name='ofonde',
            name='video',
        ),
    ]
