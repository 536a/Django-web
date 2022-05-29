# Generated by Django 3.1.7 on 2021-06-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0016_auto_20210608_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pieces',
            name='category',
            field=models.CharField(choices=[('ebru', 'EBRU'), ('heykel', 'HEYKEL'), ('cam', 'CAM'), ('resim', 'RESİM'), ('seramik', 'SERAMİK'), ('deri', 'DERİ'), ('fotograf', 'FOTOĞRAF'), ('oymacılık', 'OYMACILIK'), ('cini', 'ÇİNİ')], default='resim', max_length=20),
        ),
    ]