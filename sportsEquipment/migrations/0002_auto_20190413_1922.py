# Generated by Django 2.1.5 on 2019-04-13 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsEquipment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipmentrequest',
            old_name='eqpId',
            new_name='eqp',
        ),
        migrations.RenameField(
            model_name='equipmentrequest',
            old_name='userId',
            new_name='user',
        ),
    ]
