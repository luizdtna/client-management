# Generated by Django 2.2.4 on 2019-08-25 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCliente', '0013_auto_20190825_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='appCliente.Pessoa'),
        ),
    ]