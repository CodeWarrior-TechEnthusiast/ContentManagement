# Generated by Django 4.1.4 on 2022-12-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WriteaBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_content', models.TextField()),
                ('blog_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
