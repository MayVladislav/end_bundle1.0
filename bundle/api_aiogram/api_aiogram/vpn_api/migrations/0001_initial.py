# Generated by Django 5.0.3 on 2024-03-21 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VpnTypeModel1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vpn_type_name', models.CharField(db_index=True, max_length=30)),
            ],
            options={
                'verbose_name': 'VPN тип конфигурации',
                'verbose_name_plural': 'VPN тип конфигураций',
            },
        ),
        migrations.CreateModel(
            name='VpnUserUseModel1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('config_name', models.CharField(max_length=30)),
                ('time_exp', models.DateTimeField()),
                ('time_take', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'VPN использование конфигураций пользователями',
                'verbose_name_plural': 'VPN использования конфигураций пользователями',
            },
        ),
        migrations.CreateModel(
            name='VpnModel1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default=None, max_length=255, null=True, unique=True)),
                ('date_expired', models.DateTimeField(default=None, null=True)),
                ('url', models.CharField(max_length=1255)),
                ('photo_url', models.ImageField(default=None, null=True, upload_to='images/%Y/%m/%d/')),
                ('type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='vpn_api.vpntypemodel1')),
            ],
            options={
                'verbose_name': 'VPN конфигурация',
                'verbose_name_plural': 'VPN конфигурации',
            },
        ),
    ]
