# Generated by Django 3.2.4 on 2021-06-10 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210610_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.region'),
        ),
    ]
