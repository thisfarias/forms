# Generated by Django 3.2.8 on 2021-11-11 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atratividade', '0005_alter_client_last_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='last_data',
            field=models.DateField(default=datetime.date(2021, 11, 11)),
        ),
    ]
