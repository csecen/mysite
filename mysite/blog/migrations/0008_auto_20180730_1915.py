# Generated by Django 2.0.4 on 2018-07-30 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_comment_authorize'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_authorize',
            new_name='comment_authorized',
        ),
    ]