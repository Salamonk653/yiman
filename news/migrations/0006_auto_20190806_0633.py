# Generated by Django 2.2.1 on 2019-08-06 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20190805_0706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'ordering': ['-id'], 'verbose_name': 'Жаңылык', 'verbose_name_plural': 'Жаңылыктар'},
        ),
        migrations.AlterField(
            model_name='kairymduuluk',
            name='kurbandyk',
            field=models.IntegerField(default=0, verbose_name='Курбандыкка'),
        ),
        migrations.AlterField(
            model_name='ofonde',
            name='adres',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Дарек'),
        ),
    ]