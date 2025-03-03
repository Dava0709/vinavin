# Generated by Django 5.1.3 on 2024-11-07 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinavin_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='events',
            name='dress_code',
            field=models.CharField(max_length=600, verbose_name='Требования к одежде'),
        ),
    ]
