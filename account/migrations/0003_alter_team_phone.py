# Generated by Django 3.2.2 on 2021-07-14 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_team_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='phone',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
