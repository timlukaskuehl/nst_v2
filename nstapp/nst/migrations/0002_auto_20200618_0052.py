# Generated by Django 3.0.6 on 2020-06-17 22:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nst', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinput',
            name='image_name',
        ),
        migrations.RemoveField(
            model_name='userinput',
            name='user_name',
        ),
        migrations.AddField(
            model_name='userinput',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinput',
            name='paintings_name',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
    ]
