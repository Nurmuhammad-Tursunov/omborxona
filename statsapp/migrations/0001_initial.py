# Generated by Django 4.1 on 2022-09-15 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asosiyapp', '0002_alter_client_manzil'),
        ('userapp', '0005_delete_users'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField()),
                ('miqdor', models.PositiveIntegerField()),
                ('summa', models.BigIntegerField()),
                ('tolandi', models.BigIntegerField()),
                ('nasiya', models.BigIntegerField()),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('ombor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.ombor')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiyapp.product')),
            ],
        ),
    ]