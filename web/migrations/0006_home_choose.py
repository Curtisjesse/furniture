# Generated by Django 4.2.7 on 2023-11-28 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_rename_created_on_blog_date_rename_image_blog_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_choose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('image', models.FileField(upload_to='home_choose')),
                ('description', models.TextField(max_length=250)),
            ],
        ),
    ]
