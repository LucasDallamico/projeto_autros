# Generated by Django 2.2.4 on 2020-06-28 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200628_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='modulos', to='api.dispositivo_de_saida'),
        ),
    ]
