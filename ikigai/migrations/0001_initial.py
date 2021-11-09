# Generated by Django 3.2.8 on 2021-11-08 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('key', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('profissao', models.CharField(max_length=35)),
                ('vocacao', models.CharField(max_length=35)),
                ('missao', models.CharField(max_length=35)),
                ('paixao', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Client',
            },
        ),
    ]