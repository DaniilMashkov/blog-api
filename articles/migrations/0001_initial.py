# Generated by Django 4.1.7 on 2023-03-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_created=True)),
                ('body', models.CharField(max_length=254)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]