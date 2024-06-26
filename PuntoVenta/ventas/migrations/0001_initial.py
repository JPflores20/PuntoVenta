# Generated by Django 5.0.6 on 2024-05-28 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'clientes',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=15)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'clientes',
                'verbose_name_plural': 'clientes',
            },
        ),
    ]
