# Generated by Django 3.1.7 on 2021-06-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0018_auto_20210608_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pieces',
            name='category',
            field=models.CharField(choices=[('cini', 'ÇİNİ'), ('seramik', 'SERAMİK'), ('cam', 'CAM'), ('oymacılık', 'OYMACILIK'), ('heykel', 'HEYKEL'), ('ebru', 'EBRU'), ('resim', 'RESİM'), ('fotograf', 'FOTOĞRAF'), ('deri', 'DERİ')], default='resim', max_length=20),
        ),
    ]
