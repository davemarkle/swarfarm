# Generated by Django 2.2.15 on 2020-08-08 23:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_log', '0023_auto_20200804_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dungeonartifactdrop',
            name='archetype',
            field=models.CharField(blank=True, choices=[('attack', 'Attack'), ('hp', 'HP'), ('support', 'Support'), ('defense', 'Defense'), ('material', 'Material')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='dungeonartifactdrop',
            name='effects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, choices=[(1, 'ATK+ Proportional to Lost HP'), (2, 'DEF+ Proportional to Lost HP'), (3, 'SPD+ Proportional to Lost HP'), (4, 'SPD Under Inability'), (5, 'ATK Increased'), (6, 'DEF Increased'), (7, 'SPD Increased'), (8, 'CRI Rate Increased'), (9, 'Counterattack Damage Increased'), (10, 'Cooperative Attack Damage Increased'), (11, 'Bomb Damage Increased'), (12, 'Reflected Damage Increased'), (13, 'Crushing Hit Damage Increased'), (14, 'Damage Received Under Inability Decreased'), (15, 'Crit Damage Received Decreased'), (16, 'Life Drain Increased'), (17, 'HP When Revived Increased'), (18, 'Attack Bar When Revived Increased'), (19, 'Damage Increased By % of HP'), (20, 'Damage Increased By % of ATK'), (21, 'Damage Increased By % of DEF'), (22, 'Damage Increased By % of SPD'), (23, 'Damage To Fire Increased'), (24, 'Damage To Water Increased'), (25, 'Damage To Wind Increased'), (26, 'Damage To Light Increased'), (27, 'Damage To Dark Increased'), (28, 'Damage From Fire Decreased'), (29, 'Damage From Water Decreased'), (30, 'Damage From Wind Decreased'), (31, 'Damage From Light Decreased'), (32, 'Damage From Dark Decreased'), (33, 'Skill 1 CRI Damage Increased'), (34, 'Skill 2 CRI Damage Increased'), (35, 'Skill 3 CRI Damage Increased'), (36, 'Skill 4 CRI Damage Increased'), (37, 'Skill 1 Recovery Increased'), (38, 'Skill 2 Recovery Increased'), (39, 'Skill 3 Recovery Increased'), (40, 'Skill 1 Accuracy Increased'), (41, 'Skill 2 Accuracy Increased'), (42, 'Skill 3 Accuracy Increased')], null=True), blank=True, default=list, help_text='Bonus effect type', size=4),
        ),
        migrations.AlterField(
            model_name='dungeonartifactdrop',
            name='efficiency',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='dungeonartifactdrop',
            name='element',
            field=models.CharField(blank=True, choices=[('fire', 'Fire'), ('wind', 'Wind'), ('water', 'Water'), ('light', 'Light'), ('dark', 'Dark')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='dungeonartifactdrop',
            name='max_efficiency',
            field=models.FloatField(blank=True),
        ),
    ]
