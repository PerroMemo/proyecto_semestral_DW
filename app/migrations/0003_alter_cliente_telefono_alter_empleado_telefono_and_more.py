# Generated by Django 4.2.1 on 2023-06-19 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_cliente_telefono_alter_empleado_telefono_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(),
        ),
    ]