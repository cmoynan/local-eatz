# Generated by Django 5.1.3 on 2024-11-18 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessinquiry',
            name='address',
            field=models.TextField(default=''),
        ),
    ]