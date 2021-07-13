# Generated by Django 3.2.4 on 2021-07-06 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('floris', '0006_remove_flower_owner_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='owner_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]