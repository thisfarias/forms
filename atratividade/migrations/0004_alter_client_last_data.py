# Generated by Django 3.2.8 on 2021-11-08 23:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atratividade', '0003_client_last_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='last_data',
            field=models.DateField(default=datetime.date(2021, 11, 8)),
        ),
    ]
