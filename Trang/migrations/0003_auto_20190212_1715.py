# Generated by Django 2.0.4 on 2019-02-12 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trang', '0002_auto_20190212_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trangle',
            name='output',
            field=models.CharField(choices=[(1, 'Scalene'), (2, 'Equilateral'), (3, 'Isosceles'), (4, 'Incorrect')], default=1, max_length=100),
        ),
    ]
