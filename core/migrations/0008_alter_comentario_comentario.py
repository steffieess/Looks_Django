# Generated by Django 3.2.4 on 2021-06-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210610_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.CharField(max_length=50, verbose_name='Comentario'),
        ),
    ]
