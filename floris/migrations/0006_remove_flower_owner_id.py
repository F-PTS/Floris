# Generated by Django 3.2.4 on 2021-07-06 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floris', '0005_rename_owner_flower_owner_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flower',
            name='owner_id',
        ),
    ]