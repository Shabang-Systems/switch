# Generated by Django 2.2.4 on 2019-08-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='setCount',
            field=models.IntegerField(default=20),
        ),
    ]