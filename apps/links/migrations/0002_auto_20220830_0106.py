# Generated by Django 3.2.13 on 2022-08-30 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrooms',
            name='desactive_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data da Desativação'),
        ),
        migrations.AlterField(
            model_name='userrooms',
            name='update_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data da Atualização'),
        ),
    ]
