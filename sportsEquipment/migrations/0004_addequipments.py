# Generated by Django 2.2 on 2019-04-23 21:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsEquipment', '0003_equipments_eqpquantitytaken'),
    ]

    operations = [
        migrations.CreateModel(
            name='addEquipments',
            fields=[
                ('eqpId', models.AutoField(primary_key=True, serialize=False)),
                ('eqpName', models.CharField(max_length=50)),
                ('eqpQuantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]