# Generated by Django 4.2.1 on 2023-06-04 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kiado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('azon', models.IntegerField()),
                ('nev', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Kiado',
                'verbose_name_plural': 'Kiadok',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('azon', models.IntegerField()),
                ('cim', models.CharField(max_length=100)),
                ('kiadasiev', models.IntegerField(null=True)),
                ('kocka', models.IntegerField(null=True)),
                ('szinese', models.BooleanField()),
                ('kiado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdef.kiado')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmek',
            },
        ),
    ]
