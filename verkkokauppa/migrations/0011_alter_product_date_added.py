# Generated by Django 4.2.16 on 2024-11-30 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verkkokauppa', '0010_review_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
