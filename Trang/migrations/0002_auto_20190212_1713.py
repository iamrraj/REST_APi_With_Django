# Generated by Django 2.0.4 on 2019-02-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trang', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trangle',
            name='output',
            field=models.CharField(max_length=100),
        ),
    ]
