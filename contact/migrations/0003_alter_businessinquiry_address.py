# Generated by Django 5.1.3 on 2024-11-18 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_businessinquiry_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessinquiry',
            name='address',
            field=models.CharField(max_length=255),
        ),
    ]
