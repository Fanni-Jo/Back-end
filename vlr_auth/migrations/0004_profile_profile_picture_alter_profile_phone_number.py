# Generated by Django 4.0.5 on 2022-06-26 14:56

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('vlr_auth', '0003_remove_profile_birthdate_remove_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pictures/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='JO', unique=True),
        ),
    ]