# Generated by Django 2.1.15 on 2020-06-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0006_auto_20200615_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wod',
            name='coach',
            field=models.CharField(max_length=30, null=True),
        ),
    ]