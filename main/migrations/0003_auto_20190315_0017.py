# Generated by Django 2.1a1 on 2019-03-14 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190314_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='dob',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='gender',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]