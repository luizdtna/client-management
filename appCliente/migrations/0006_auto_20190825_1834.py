# Generated by Django 2.2.4 on 2019-08-25 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCliente', '0005_auto_20190825_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='appCliente.Pessoa'),
        ),
    ]
