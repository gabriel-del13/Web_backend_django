# Generated by Django 5.0.7 on 2024-09-14 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available_quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('DISPONIBLE', 'disponible'), ('AGOTADO', 'agotado'), ('PRÓXIMAMENTE', 'próximamente')], default='DISPONIBLE', max_length=20),
        ),
    ]
