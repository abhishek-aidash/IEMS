# Generated by Django 4.0.6 on 2022-08-07 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iems_api', '0002_alter_enchroachment_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Status'},
        ),
        migrations.RemoveIndex(
            model_name='status',
            name='iems_api_st_status__ad4b27_idx',
        ),
    ]
