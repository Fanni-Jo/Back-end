# Generated by Django 4.0.5 on 2022-07-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlr_auth', '0003_serviceproviderprofile_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceproviderprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile-pictures-service-providers/', verbose_name='profile picture'),
        ),
    ]