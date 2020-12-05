# Generated by Django 3.1.3 on 2020-12-05 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaAccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=100)),
                ('page_id', models.CharField(blank=True, max_length=250, null=True)),
                ('user_access_token', models.TextField(blank=True, help_text='facebook user access token(no expiry)', max_length=250, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media_handle', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Social Media Token',
                'verbose_name_plural': 'Social Media Tokens',
            },
        ),
    ]
