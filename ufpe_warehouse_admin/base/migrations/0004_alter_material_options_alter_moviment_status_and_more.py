# Generated by Django 4.2.7 on 2023-11-24 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_moviment_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='moviment',
            name='status',
            field=models.IntegerField(choices=[(1, 'entrada'), (2, 'saída')], max_length=3),
        ),
        migrations.AlterField(
            model_name='sector',
            name='sigla',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='MaterialQuantityStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_material', models.BooleanField(default=False)),
                ('local_store', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.localstore')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.material')),
            ],
        ),
        migrations.AddField(
            model_name='localstore',
            name='materials',
            field=models.ManyToManyField(through='base.MaterialQuantityStore', to='base.material'),
        ),
    ]
