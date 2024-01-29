# Generated by Django 4.2.6 on 2023-12-26 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ifichapel', '0008_alter_baptism_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedstatus',
            name='baptism',
        ),
        migrations.RemoveField(
            model_name='schedstatus',
            name='blessing',
        ),
        migrations.RemoveField(
            model_name='schedstatus',
            name='funeral',
        ),
        migrations.RemoveField(
            model_name='schedstatus',
            name='marriage',
        ),
        migrations.AddField(
            model_name='schedstatus',
            name='baptism',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ifichapel.baptism'),
        ),
        migrations.AddField(
            model_name='schedstatus',
            name='blessing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ifichapel.blessing'),
        ),
        migrations.AddField(
            model_name='schedstatus',
            name='funeral',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ifichapel.funerals'),
        ),
        migrations.AddField(
            model_name='schedstatus',
            name='marriage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ifichapel.marriage'),
        ),
    ]
