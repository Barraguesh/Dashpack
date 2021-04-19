# Generated by Django 3.1.7 on 2021-03-14 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.CharField(max_length=1000, primary_key=True, serialize=False, verbose_name='Client ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Device ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('category', models.CharField(max_length=100, verbose_name='Category')),
                ('entry_date', models.DateField(verbose_name='Entry date')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientModule.client', verbose_name='Client')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('log', models.CharField(max_length=1000, primary_key=True, serialize=False, verbose_name='Log')),
                ('date', models.DateField(max_length=1000, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.CharField(max_length=1000, primary_key=True, serialize=False, verbose_name='Ticket ID')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('log', models.TextField(verbose_name='Log')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('priority', models.IntegerField(verbose_name='Priority')),
                ('date', models.DateField(max_length=1000, verbose_name='Date')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientModule.client', verbose_name='Client')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientModule.device', verbose_name='Device')),
            ],
        ),
    ]