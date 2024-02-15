# Generated by Django 5.0.2 on 2024-02-15 07:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('page_url', models.CharField(max_length=255)),
                ('banner_type', models.CharField(choices=[('Header', 'Header'), ('Footer', 'Footer')], max_length=10)),
                ('content', models.TextField()),
                ('file', models.CharField(max_length=255)),
                ('file_type', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
