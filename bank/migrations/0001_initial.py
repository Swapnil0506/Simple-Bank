# Generated by Django 3.1.2 on 2021-07-10 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('account_no', models.CharField(max_length=20)),
                ('ifsc_code', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=100)),
                ('amount', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='trans_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=150)),
                ('sender_email', models.EmailField(max_length=254)),
                ('sender_accno', models.CharField(max_length=20)),
                ('current_balance', models.IntegerField(max_length=10)),
                ('reciever_name', models.CharField(max_length=150)),
                ('money_transfer', models.IntegerField(max_length=10)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
