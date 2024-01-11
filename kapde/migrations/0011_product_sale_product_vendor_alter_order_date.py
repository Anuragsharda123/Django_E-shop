# Generated by Django 4.1.5 on 2023-07-10 17:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kapde', '0010_company_alter_order_date_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='kapde.vendor'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 10, 22, 49, 34, 335454)),
        ),
    ]
