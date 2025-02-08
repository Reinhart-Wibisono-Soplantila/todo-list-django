# Generated by Django 5.1.6 on 2025-02-08 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_category_created_at_category_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
