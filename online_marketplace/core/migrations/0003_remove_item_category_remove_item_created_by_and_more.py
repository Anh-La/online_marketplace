# Generated by Django 5.0.3 on 2024-03-26 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
