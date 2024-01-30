# Generated by Django 4.2.6 on 2023-10-31 20:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0004_movie_img1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='img1',
        ),
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='static'),
            preserve_default=False,
        ),
    ]