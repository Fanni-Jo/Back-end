# Generated by Django 4.0.5 on 2022-06-27 10:34

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('vlr_auth', '0012_remove_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='phone no.'),
        ),
    ]
