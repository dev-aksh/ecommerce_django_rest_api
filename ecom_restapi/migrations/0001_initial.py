# Generated by Django 3.0.2 on 2020-07-15 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('product_category', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('product_subcategory', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom_restapi.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('product_title', models.CharField(max_length=85)),
                ('unitprice', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('totalprice', models.FloatField()),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom_restapi.Categories')),
                ('product_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom_restapi.SubCategories')),
            ],
        ),
    ]
