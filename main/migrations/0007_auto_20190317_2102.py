# Generated by Django 2.1a1 on 2019-03-17 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190317_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='gender',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
