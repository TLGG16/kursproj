# Generated by Django 4.0.4 on 2022-05-15 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kursach', '0004_product_details_alter_supplier_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kursach.supplier'),
        ),
    ]