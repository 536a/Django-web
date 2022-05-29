# Generated by Django 3.1.7 on 2021-06-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0017_auto_20210608_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pieces',
            name='category',
            field=models.CharField(choices=[('seramik', 'SERAMİK'), ('resim', 'RESİM'), ('heykel', 'HEYKEL'), ('cini', 'ÇİNİ'), ('oymacılık', 'OYMACILIK'), ('ebru', 'EBRU'), ('cam', 'CAM'), ('deri', 'DERİ'), ('fotograf', 'FOTOĞRAF')], default='resim', max_length=20),
        ),
    ]