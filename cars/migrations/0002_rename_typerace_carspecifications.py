# Generated by Django 3.2.3 on 2021-05-31 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TypeRace',
            new_name='CarSpecifications',
        ),
    ]