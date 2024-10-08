# Generated by Django 5.0.6 on 2024-07-16 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_barras', models.CharField(max_length=100, unique=True)),
                ('producto', models.CharField(max_length=50)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.ImageField(upload_to='')),
            ],
        ),
    ]
