# Generated by Django 2.0.4 on 2018-07-30 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180729_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_authorize',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]