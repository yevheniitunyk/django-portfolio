# Generated by Django 4.2 on 2023-04-07 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliomodel',
            name='description',
            field=models.TextField(),
        ),
    ]
