# Generated by Django 4.0.6 on 2022-08-07 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iems_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enchroachment',
            unique_together={('department_name', 'status_name', 'enchrt_id')},
        ),
    ]
