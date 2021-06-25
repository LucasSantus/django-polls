# Generated by Django 3.0.13 on 2021-06-24 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=194, verbose_name='Nome Completo:')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF:')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento:')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail:')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Votacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=194, verbose_name='Título:')),
                ('descricao', models.TextField(max_length=340, verbose_name='Descrição:')),
                ('anonimo', models.BooleanField(default=False, verbose_name='Usuário Anônimo:')),
                ('data_inicio', models.DateTimeField(blank=True, null=True, verbose_name='Inicio:')),
                ('data_fim', models.DateTimeField(blank=True, null=True, verbose_name='Término:')),
            ],
            options={
                'verbose_name': 'Votação',
                'verbose_name_plural': 'Votações',
            },
        ),
        migrations.CreateModel(
            name='OpcaoVoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=194, verbose_name='Nome')),
                ('codigo', models.CharField(max_length=194, verbose_name='Código:')),
                ('numero_votos', models.PositiveSmallIntegerField(default=0, verbose_name='Número de Voto:')),
                ('votacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Votacao', verbose_name='Votação:')),
            ],
            options={
                'verbose_name': 'Opcão de Voto',
                'verbose_name_plural': 'Opções de Votos',
            },
        ),
    ]
