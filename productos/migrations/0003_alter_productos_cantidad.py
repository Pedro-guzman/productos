# Generated by Django 5.0.6 on 2024-07-17 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_productos_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='cantidad',
            field=models.IntegerField(blank=True),
        ),
    ]
