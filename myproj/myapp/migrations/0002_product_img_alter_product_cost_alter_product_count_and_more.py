# Generated by Django 4.2.5 on 2024-11-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, upload_to='myapp/static/img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.IntegerField(verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.IntegerField(verbose_name='Кол-во на складе'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='dod',
            field=models.DateField(auto_now=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
    ]
