# Generated by Django 2.2.4 on 2020-06-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dispositivo_de_saida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name_plural': 'Dispositivos de saida',
            },
        ),
    ]
