# Generated by Django 3.2.4 on 2021-06-22 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('floris', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('water_time', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='flowers',
            old_name='owner',
            new_name='owner_id',
        ),
        migrations.RemoveField(
            model_name='flowers',
            name='name',
        ),
        migrations.AddField(
            model_name='flowers',
            name='plant_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='floris.flower'),
        ),
    ]