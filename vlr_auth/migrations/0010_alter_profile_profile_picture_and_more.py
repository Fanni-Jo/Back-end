# Generated by Django 4.0.5 on 2022-07-06 13:06

from django.db import migrations, models
import vlr_auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('vlr_auth', '0009_alter_reviewworkerrating_service_provider_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=vlr_auth.models.upload_path),
        ),
        migrations.AlterField(
            model_name='serviceproviderprofile',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to=vlr_auth.models.upload_path_media, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='serviceproviderprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=vlr_auth.models.upload_path, verbose_name='profile picture'),
        ),
    ]
