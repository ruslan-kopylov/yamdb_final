# Generated by Django 2.2.16 on 2022-04-19 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220419_0601'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('pub_date',)},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('pub_date',)},
        ),
    ]
