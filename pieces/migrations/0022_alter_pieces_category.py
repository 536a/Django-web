# Generated by Django 3.2 on 2021-06-20 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0021_auto_20210612_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pieces',
            name='category',
            field=models.CharField(choices=[('cam', 'CAM'), ('heykel', 'HEYKEL'), ('cini', 'ÇİNİ'), ('fotograf', 'FOTOĞRAF'), ('resim', 'RESİM'), ('seramik', 'SERAMİK'), ('ebru', 'EBRU'), ('deri', 'DERİ'), ('oymacılık', 'OYMACILIK')], default='resim', max_length=20),
        ),
    ]