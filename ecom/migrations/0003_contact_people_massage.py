# Generated by Django 4.2.4 on 2023-08-31 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_product_shop_site_productdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_header_h2', models.CharField(max_length=255)),
                ('page_header_p', models.TextField()),
                ('details_span', models.CharField(max_length=255)),
                ('details_h2', models.TextField()),
                ('details_h3', models.CharField(max_length=255)),
                ('details_map', models.TextField()),
                ('details_env', models.TextField()),
                ('details_phone', models.TextField()),
                ('details_hours', models.TextField()),
                ('map', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('job', models.TextField()),
                ('img', models.ImageField(upload_to='static/img/')),
                ('phone', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('msg', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='msgs', to='ecom.people')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='ecom.customer')),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
    ]
