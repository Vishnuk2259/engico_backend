# Generated by Django 5.0.2 on 2024-03-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0006_alter_settings_facebook_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='linkedin_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='twitter_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]