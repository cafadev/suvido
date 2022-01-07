# Generated by Django 3.1.6 on 2022-01-06 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('thumbnail', models.ImageField(null=True, upload_to='thumbnails/')),
                ('download_times', models.PositiveIntegerField(default=0)),
                ('channel', models.CharField(max_length=255)),
                ('duration', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
