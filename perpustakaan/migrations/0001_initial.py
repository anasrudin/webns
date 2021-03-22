# Generated by Django 3.1.7 on 2021-03-22 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodebuku', models.CharField(max_length=255)),
                ('judulbuku', models.CharField(max_length=255)),
                ('pengarang', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pinjam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nislokal', models.CharField(max_length=255)),
                ('nama', models.CharField(max_length=255)),
                ('tanggalpinjam', models.DateField()),
                ('tanggalkembali', models.DateField()),
                ('buku', models.ManyToManyField(to='perpustakaan.Buku')),
            ],
        ),
    ]
