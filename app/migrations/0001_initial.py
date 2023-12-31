# Generated by Django 5.0 on 2023-12-17 18:06

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_title', models.CharField(max_length=1000)),
                ('category_image', models.ImageField(upload_to='photos')),
                ('category_description', ckeditor.fields.RichTextField()),
                ('category_date', models.DateTimeField()),
                ('url', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('tutorial_id', models.AutoField(primary_key=True, serialize=False)),
                ('tutorial_name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_title', models.CharField(max_length=1000)),
                ('blog_image', models.ImageField(upload_to='photos')),
                ('blog_description', ckeditor.fields.RichTextField()),
                ('blog_date', models.DateTimeField()),
                ('url', models.CharField(max_length=100, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=100)),
                ('post_file', models.FileField(upload_to='photos')),
                ('post_description', ckeditor.fields.RichTextField()),
                ('post_date', models.DateTimeField()),
                ('url', models.CharField(max_length=100, unique=True)),
                ('tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tutorial')),
            ],
        ),
    ]
