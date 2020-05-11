# Generated by Django 3.0.6 on 2020-05-10 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eqname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='referancename',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='inservice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make1', models.CharField(max_length=30)),
                ('srno1', models.CharField(max_length=30)),
                ('make2', models.CharField(max_length=30)),
                ('srno2', models.CharField(max_length=30)),
                ('eqname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insform.eqname')),
                ('referancename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insform.referancename')),
            ],
        ),
    ]
