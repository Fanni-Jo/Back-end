# Generated by Django 4.0.5 on 2022-07-05 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlr_auth', '0007_alter_serviceproviderprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceproviderprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='serviceproviderprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='last_name'),
        ),
    ]
