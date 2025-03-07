# Generated by Django 4.2 on 2023-05-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_shipment_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='shipment',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='shipment',
            name='date1',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='shipment',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
