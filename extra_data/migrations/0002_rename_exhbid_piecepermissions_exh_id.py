# Generated by Django 3.2 on 2021-05-14 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piecepermissions',
            old_name='exhbid',
            new_name='exh_id',
        ),
    ]
