# Generated by Django 3.0.3 on 2020-11-03 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0002_auto_20200925_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_json', models.CharField(max_length=5000)),
                ('user_name', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=500)),
                ('address2', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('order_total', models.IntegerField()),
            ],
        ),
    ]
