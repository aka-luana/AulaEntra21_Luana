# Generated by Django 3.1.5 on 2021-01-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
