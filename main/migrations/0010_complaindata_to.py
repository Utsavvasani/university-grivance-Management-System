# Generated by Django 4.1 on 2023-05-01 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_designation_user_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaindata',
            name='to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.designation'),
        ),
    ]
