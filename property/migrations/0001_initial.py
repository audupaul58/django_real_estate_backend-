# Generated by Django 4.1 on 2022-09-20 18:13

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mytags', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Bungalow', 'bungalow'), ('Duplex', 'duplex'), ('Mansion', 'mansion'), ('Lekki', 'Lekki')], default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('tags', multiselectfield.db.fields.MultiSelectField(choices=[('Bungalow', 'bungalow'), ('Duplex', 'duplex'), ('Mansion', 'mansion'), ('Lekki', 'Lekki')], max_length=150)),
                ('description', models.TextField()),
                ('images', models.ImageField(upload_to='')),
                ('category', models.CharField(choices=[('sale', 'sale'), ('rent', 'rent'), ('land', 'land')], default=None, max_length=50)),
                ('prices', models.DecimalField(decimal_places=1, max_digits=11)),
                ('rooms', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('rentFrequencies', models.CharField(choices=[('None', None), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')], default=None, max_length=50)),
                ('area', models.DecimalField(decimal_places=2, max_digits=5)),
                ('isVerify', models.BooleanField(default=False)),
                ('agency', models.ImageField(upload_to='')),
                ('myamenity', multiselectfield.db.fields.MultiSelectField(choices=[('Washers and dryers', 'Washers and dryers'), ('Central air conditioning', 'Central air conditioning'), ('Forced air heating', 'Forced air heating'), ('Balconies', 'Balconies'), ('Smart-home features', 'Smart-home features'), ('Wi-Fi', 'Wi-Fi'), ('High-speed internet', 'High-speed internet'), ('Security', 'Security'), ('CCTV Camera', 'CCTV Camera'), ('High-end fixtures and finishes', 'High-end fixtures and finishes'), ('Renovated spaces', 'Renovated spaces'), ('Open floor plans', 'Open floor plans'), ('Pet-friendly spaces', 'Pet-friendly spaces'), ('Stainless steel appliances', 'Stainless steel appliances'), ('Closets or storage space', 'Closets or storage space'), ('Large windows and natural light', 'Large windows and natural light')], default=None, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('created_at__month',))),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='PropsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(null=True, upload_to='images/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='property.property')),
            ],
        ),
    ]