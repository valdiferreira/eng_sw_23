# Generated by Django 4.2.7 on 2023-11-24 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_moviment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialquantitystore',
            name='quantity_material',
            field=models.IntegerField(),
        ),
    ]
