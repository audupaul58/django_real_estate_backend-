# Generated by Django 4.1 on 2022-09-25 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_salemodel_salesimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesimage',
            old_name='property',
            new_name='salemodel',
        ),
    ]
