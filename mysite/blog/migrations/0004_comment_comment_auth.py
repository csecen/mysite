# Generated by Django 2.0.4 on 2018-07-29 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_read_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_auth',
            field=models.CharField(default='Me', max_length=50),
            preserve_default=False,
        ),
    ]
