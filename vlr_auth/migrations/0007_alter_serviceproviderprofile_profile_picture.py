# Generated by Django 4.0.5 on 2022-07-04 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlr_auth', '0006_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceproviderprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile-pictures-service-providers/', verbose_name='profile picture'),
        ),
    ]
