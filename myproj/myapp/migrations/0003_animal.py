# Generated by Django 4.2.5 on 2024-11-24 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product_img_alter_product_cost_alter_product_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sound', models.CharField(max_length=100)),
            ],
        ),
    ]
