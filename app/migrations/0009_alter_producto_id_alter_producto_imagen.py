# Generated by Django 4.2.1 on 2023-06-20 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_producto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='app/db_img/'),
        ),
    ]