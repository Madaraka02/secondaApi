# Generated by Django 3.2.8 on 2021-10-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyjobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='apply',
            field=models.BooleanField(default=False),
        ),
    ]
