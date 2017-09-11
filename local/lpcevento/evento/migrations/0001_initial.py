# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtigoCientifico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('eventoPrincipal', models.CharField(max_length=128, null=True)),
                ('sigla', models.CharField(max_length=128, null=True)),
                ('dataEHoraDeInicio', models.DateTimeField(blank=True, null=True)),
                ('palavrasChave', models.CharField(max_length=128, null=True)),
                ('logoTipo', models.CharField(max_length=128, null=True)),
                ('cidade', models.CharField(max_length=128)),
                ('uf', models.CharField(max_length=128)),
                ('endereco', models.CharField(max_length=128, null=True)),
                ('cep', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.Pessoa')),
                ('curriculo', models.CharField(max_length=128)),
                ('artigos', models.ManyToManyField(to='evento.ArtigoCientifico')),
            ],
            bases=('evento.pessoa',),
        ),
        migrations.CreateModel(
            name='EventoCientifico',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.Evento')),
                ('issn', models.CharField(max_length=128)),
            ],
            bases=('evento.evento',),
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.Pessoa')),
                ('cpf', models.CharField(max_length=11)),
            ],
            bases=('evento.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.Pessoa')),
                ('cnpj', models.CharField(max_length=15)),
                ('razaoSocial', models.CharField(max_length=128)),
            ],
            bases=('evento.pessoa',),
        ),
        migrations.AddField(
            model_name='evento',
            name='realizador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='evento.Pessoa'),
        ),
        migrations.AddField(
            model_name='artigocientifico',
            name='autores',
            field=models.ManyToManyField(to='evento.Autor'),
        ),
        migrations.AddField(
            model_name='artigocientifico',
            name='evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='evento.EventoCientifico'),
        ),
    ]
