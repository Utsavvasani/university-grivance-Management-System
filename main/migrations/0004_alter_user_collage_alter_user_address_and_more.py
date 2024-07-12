# Generated by Django 4.1.7 on 2023-04-30 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_complaindata_complaincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Collage',
            field=models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.collage'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.department'),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.designation'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fatherName',
            field=models.TextField(default='NULL', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(default='NULL', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='semester',
            field=models.IntegerField(default='NULL', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='surName',
            field=models.TextField(default='NULL', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='userName',
            field=models.TextField(default='NULL', max_length=20),
        ),
    ]
