# Generated by Django 3.2.9 on 2021-11-26 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppGalenos', '0003_hora_medico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hora',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='AppGalenos.paciente'),
        ),
    ]