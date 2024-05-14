# Generated by Django 4.2.6 on 2024-02-23 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RentItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover', models.ImageField(upload_to='rent_items')),
                ('rent_per_day', models.FloatField()),
            ],
        ),
    ]
