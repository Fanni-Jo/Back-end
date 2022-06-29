# Generated by Django 4.0.5 on 2022-06-29 21:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vlr_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, max_length=3000)),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewWorkerRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('review', models.TextField(blank=True, max_length=500)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProviderProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='phone no.')),
                ('phone2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='secondary phone no.')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('address', models.TextField(verbose_name='address')),
                ('years_of_exp', models.IntegerField(verbose_name='experience')),
                ('media', models.FileField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default=None, max_length=6)),
            ],
            options={
                'verbose_name': 'service provider',
                'verbose_name_plural': 'service providers',
                'ordering': ('-date',),
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Category'),
        ),
        migrations.DeleteModel(
            name='WorkerProfile',
        ),
        migrations.AddField(
            model_name='serviceproviderprofile',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vlr_auth.category', verbose_name='Category '),
        ),
        migrations.AddField(
            model_name='serviceproviderprofile',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewworkerrating',
            name='service_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vlr_auth.serviceproviderprofile'),
        ),
    ]
