# Generated by Django 3.1.2 on 2021-07-11 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='full_name',
            new_name='name',
        ),
    ]
