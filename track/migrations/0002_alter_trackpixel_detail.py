# Generated by Django 5.1 on 2024-08-29 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackpixel',
            name='detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='track.trackdetail'),
        ),
    ]
