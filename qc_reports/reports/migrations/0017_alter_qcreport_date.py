# Generated by Django 3.2.8 on 2021-10-24 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0016_alter_corereadings_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qcreport',
            name='date',
            field=models.DateField(),
        ),
    ]