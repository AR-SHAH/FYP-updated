# Generated by Django 3.2.7 on 2021-09-27 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=8000)),
                ('polarity', models.CharField(max_length=10)),
                ('score', models.PositiveSmallIntegerField()),
                ('Product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='mainApp.product')),
            ],
        ),
    ]
