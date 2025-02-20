# Generated by Django 5.1.2 on 2024-10-10 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('customer_type', models.CharField(choices=[('Organizational', 'Organizational'), ('Private', 'Private')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('make', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField()),
                ('lead_time', models.IntegerField(help_text='Lead time in days')),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('enquiry_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquiry.customer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquiry.item')),
            ],
        ),
    ]
