# Generated by Django 2.1.3 on 2018-11-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sw_parser', '0011_auto_20181119_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magicboxcraft',
            name='box_type',
            field=models.IntegerField(choices=[(0, 'Unknown Magic Box'), (1, 'Mystical Magic Box'), (2, 'Legendary Magic Box')]),
        ),
    ]
