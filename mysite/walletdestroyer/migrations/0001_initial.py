# Generated by Django 4.2.4 on 2023-09-14 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EarningModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.PositiveIntegerField()),
                ('time_create', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SpendingTypesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SpendingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('spending_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='walletdestroyer.spendingtypesmodel')),
            ],
        ),
    ]
