# Generated by Django 2.1 on 2018-08-27 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weather',
            old_name='location',
            new_name='city',
        ),
    ]
