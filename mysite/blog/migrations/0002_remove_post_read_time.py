# Generated by Django 2.1.1 on 2018-09-06 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='read_time',
        ),
    ]
