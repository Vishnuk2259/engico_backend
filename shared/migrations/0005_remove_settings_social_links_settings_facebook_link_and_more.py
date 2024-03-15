# Generated by Django 5.0.2 on 2024-03-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0004_alter_brand_description_alter_category_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='social_links',
        ),
        migrations.AddField(
            model_name='settings',
            name='facebook_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='instagram_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='linkedin_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='twitter_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]