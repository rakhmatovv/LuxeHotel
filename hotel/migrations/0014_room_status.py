# Generated by Django 4.1.6 on 2023-03-01 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0013_alter_booking_check_in_alter_booking_check_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
