# Generated by Django 4.1.6 on 2023-02-06 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
