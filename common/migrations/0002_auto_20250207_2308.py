# Generated by Django 3.2.6 on 2025-02-07 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Statuses'},
        ),
    ]
