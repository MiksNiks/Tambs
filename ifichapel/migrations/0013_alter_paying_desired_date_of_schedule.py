# Generated by Django 4.2.6 on 2024-01-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifichapel', '0012_paying_remove_marriage_desired_marriage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paying',
            name='desired_date_of_schedule',
            field=models.CharField(max_length=150),
        ),
    ]