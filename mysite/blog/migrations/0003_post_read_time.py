# Generated by Django 2.0.4 on 2018-07-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180728_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read_time',
            field=models.CharField(default='5 mins', max_length=15),
            preserve_default=False,
        ),
    ]