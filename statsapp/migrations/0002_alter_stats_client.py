# Generated by Django 4.1 on 2022-09-15 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiyapp', '0002_alter_client_manzil'),
        ('statsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiyapp.client'),
        ),
    ]
