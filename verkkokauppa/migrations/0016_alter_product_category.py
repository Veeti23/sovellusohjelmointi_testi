# Generated by Django 5.1.4 on 2024-12-11 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verkkokauppa', '0015_product_category_product_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(help_text='Tuotekategoria', max_length=50),
        ),
    ]