# Generated by Django 3.2.4 on 2021-07-06 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floris', '0004_auto_20210701_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flower',
            old_name='owner',
            new_name='owner_id',
        ),
    ]
