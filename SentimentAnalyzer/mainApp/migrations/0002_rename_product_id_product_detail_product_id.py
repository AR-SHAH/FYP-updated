# Generated by Django 3.2.7 on 2021-09-27 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_detail',
            old_name='Product_id',
            new_name='product_id',
        ),
    ]
