# Generated by Django 4.2.6 on 2023-12-03 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ifichapel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baptism',
            old_name='contact',
            new_name='contact_number',
        ),
        migrations.RenameField(
            model_name='baptism',
            old_name='chilfuname',
            new_name='full_child_name',
        ),
        migrations.RenameField(
            model_name='baptism',
            old_name='fufather',
            new_name='full_father_name',
        ),
        migrations.RenameField(
            model_name='baptism',
            old_name='fumother',
            new_name='full_mother_name',
        ),
        migrations.RenameField(
            model_name='baptism',
            old_name='national',
            new_name='nationality',
        ),
        migrations.RenameField(
            model_name='baptism',
            old_name='xeroxbir',
            new_name='xerox_copy_birthcertificate',
        ),
    ]
