# Generated by Django 4.1 on 2023-05-01 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_complaindata_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaindata',
            name='feedback',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
