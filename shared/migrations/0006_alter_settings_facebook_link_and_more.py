# Generated by Django 5.0.2 on 2024-03-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0005_remove_settings_social_links_settings_facebook_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='facebook_link',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='instagram_link',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='linkedin_link',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='twitter_link',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
