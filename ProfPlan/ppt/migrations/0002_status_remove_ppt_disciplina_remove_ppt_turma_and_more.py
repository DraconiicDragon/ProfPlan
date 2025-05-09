# Generated by Django 5.2 on 2025-05-10 22:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disciplinas', '0004_disciplinaprofessor'),
        ('ppt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='ppt',
            name='disciplina',
        ),
        migrations.RemoveField(
            model_name='ppt',
            name='turma',
        ),
        migrations.RemoveField(
            model_name='ppt',
            name='usuario',
        ),
        migrations.CreateModel(
            name='PedidoPpt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrega', models.DateField()),
                ('disciplinaProfessor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disciplinas.disciplinaprofessor')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ppt.status')),
            ],
        ),
        migrations.AddField(
            model_name='ppt',
            name='pedido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ppt.pedidoppt'),
            preserve_default=False,
        ),
    ]
