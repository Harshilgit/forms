# Generated by Django 3.0.6 on 2020-05-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testpoint', models.CharField(max_length=15)),
                ('deviation1', models.CharField(max_length=15)),
                ('deviation2', models.CharField(max_length=15)),
                ('difference', models.CharField(max_length=15)),
                ('uncertainity', models.CharField(max_length=15)),
                ('remark', models.CharField(max_length=15)),
            ],
        ),
    ]
