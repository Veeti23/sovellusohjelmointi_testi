# Generated by Django 4.2.16 on 2024-11-29 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verkkokauppa', '0006_remove_productdetail_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='detail',
            field=models.CharField(help_text='Lisää tuotteen tarkempi kuvaus', max_length=400),
        ),
    ]