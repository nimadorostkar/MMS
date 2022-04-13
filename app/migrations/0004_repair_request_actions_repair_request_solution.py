# Generated by Django 4.0.4 on 2022-04-13 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_component_request_deliverytime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair_request',
            name='Actions',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='اقدامات انجام شده'),
        ),
        migrations.AddField(
            model_name='repair_request',
            name='Solution',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='راه حل'),
        ),
    ]