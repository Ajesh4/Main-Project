# Generated by Django 4.2.6 on 2024-04-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0002_bookarcappointment_status_plans_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='works',
            name='desc',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
