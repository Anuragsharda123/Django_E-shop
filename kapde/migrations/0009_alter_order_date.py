# Generated by Django 4.1.5 on 2023-05-13 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapde', '0008_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 13, 16, 0, 38, 895152)),
        ),
    ]
