# Generated by Django 3.0.8 on 2020-08-09 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200808_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default=1, max_length=130),
            preserve_default=False,
        ),
    ]