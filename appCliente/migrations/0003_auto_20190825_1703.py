# Generated by Django 2.2.4 on 2019-08-25 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCliente', '0002_pessoa_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_doc', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pessoa',
            name='doc',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appCliente.Document'),
        ),
    ]
