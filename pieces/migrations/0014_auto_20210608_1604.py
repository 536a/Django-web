# Generated by Django 3.1.7 on 2021-06-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0013_auto_20210605_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pieces',
            name='category',
            field=models.CharField(choices=[('heykel', 'HEYKEL'), ('cini', 'ÇİNİ'), ('cam', 'CAM'), ('deri', 'DERİ'), ('seramik', 'SERAMİK'), ('fotograf', 'FOTOĞRAF'), ('ebru', 'EBRU'), ('oymacılık', 'OYMACILIK'), ('resim', 'RESİM')], default='resim', max_length=20),
        ),
    ]
