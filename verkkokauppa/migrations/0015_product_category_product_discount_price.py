# Generated by Django 5.1.4 on 2024-12-11 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verkkokauppa', '0014_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='Muut', help_text='Tuotekategoria', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Alennushinta', max_digits=8, null=True),
        ),
    ]
