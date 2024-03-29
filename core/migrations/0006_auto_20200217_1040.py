# Generated by Django 2.2 on 2020-02-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200217_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('WTT', 'Womens T-shirts & Tanks'), ('WT', 'Womens Tops'), ('WOJ', 'Womens Outwear & Jackets'), ('WSC', 'Womens Sweaters & Cardigans'), ('WJ', 'Womens Jeans'), ('WL', 'Womens Leggings'), ('WP', 'Womens Pants'), ('WSS', 'Womens Skirts & Shorts'), ('WA', 'Womens Accessories'), ('WT', 'Womens Tops'), ('WHSS', ' Womans Hoodies and Sweat Shirts'), ('MTT', 'Mens T-shirts & Tanks'), ('MT', 'Mens Tops'), ('MOJ', 'Mens Outwear & Jackets'), ('MSC', 'Mens Sweaters & Cardigans'), ('MS', 'Mens Shirts'), ('MP', 'Mens Pants'), ('MA', 'Mens Accessories'), ('MHSS', 'Mens Hoodies and Sweat Shirts'), ('UTT', 'Unisex T-shirts & Tanks'), ('UT', 'Unisex Tops'), ('UHSS', 'Unisex Hoodies and Sweat Shirts'), ('UOJ', 'Unisex Outwear & Jackets'), ('USC', 'Unisex Sweaters & Cardigans'), ('UJ', 'Unisex Jeans'), ('UL', 'Unisex Leggings'), ('UP', 'Unisex Pants'), ('USS', 'Unisex Skirts & Shorts'), ('UA', 'Unisex Accessories')], max_length=2),
        ),
    ]
