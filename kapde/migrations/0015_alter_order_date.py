# Generated by Django 4.1.5 on 2024-02-19 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapde', '0014_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.date(2024, 2, 19)),
        ),
    ]
