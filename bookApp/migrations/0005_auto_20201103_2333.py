# Generated by Django 3.0.3 on 2020-11-03 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0004_order_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.CharField(max_length=100),
        ),
    ]
