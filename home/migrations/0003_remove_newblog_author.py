# Generated by Django 4.2.2 on 2023-06-20 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_newblog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newblog',
            name='author',
        ),
    ]
