# Generated by Django 2.1a1 on 2019-03-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190315_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
