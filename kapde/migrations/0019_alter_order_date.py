# Generated by Django 4.1.5 on 2024-02-19 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapde', '0018_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 2, 19, 16, 28, 37, 243948, tzinfo=datetime.timezone.utc)),
        ),
    ]
