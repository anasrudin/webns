# Generated by Django 3.0.8 on 2021-03-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nisn', models.CharField(max_length=255)),
                ('nik', models.CharField(max_length=255)),
                ('tempatlahir', models.CharField(max_length=255)),
            ],
        ),
    ]
