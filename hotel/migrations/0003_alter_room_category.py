# Generated by Django 4.1.6 on 2023-02-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_room_delete_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('BOR', 'BORA'), ('DEL', 'DELUXE'), ('LUX', 'LUXE')], max_length=3),
        ),
    ]