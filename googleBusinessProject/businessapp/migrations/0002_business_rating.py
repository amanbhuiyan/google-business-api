# Generated by Django 4.2.6 on 2023-10-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='rating',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
