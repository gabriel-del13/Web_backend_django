# Generated by Django 5.0.7 on 2024-09-03 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_cart_tables'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='products.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('DISPONIBLE', 'disponible'), ('AGOTADO', 'agotado'), ('PRÓXIMAMENTE', 'próximamente')], default='DISPONIBLE', max_length=20),
        ),
    ]