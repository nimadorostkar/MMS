# Generated by Django 4.0.4 on 2022-04-13 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_outside_manufacture_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacture_request',
            name='Management_approval',
            field=models.BooleanField(default=False, verbose_name='تایید مدیریت'),
        ),
        migrations.AddField(
            model_name='manufacture_request',
            name='Molding_office_approval',
            field=models.BooleanField(default=False, verbose_name='تایید دفتر قالبسازی'),
        ),
        migrations.AddField(
            model_name='manufacture_request',
            name='QC_approval',
            field=models.BooleanField(default=False, verbose_name='تایید مدیریت کیفیت و تولید'),
        ),
        migrations.AddField(
            model_name='outside_manufacture_request',
            name='Management_approval',
            field=models.BooleanField(default=False, verbose_name='تایید مدیریت'),
        ),
        migrations.AddField(
            model_name='outside_manufacture_request',
            name='Molding_office_approval',
            field=models.BooleanField(default=False, verbose_name='تایید دفتر قالبسازی'),
        ),
        migrations.AddField(
            model_name='outside_manufacture_request',
            name='QC_approval',
            field=models.BooleanField(default=False, verbose_name='تایید مدیریت کیفیت و تولید'),
        ),
        migrations.AddField(
            model_name='repair_request',
            name='Management_approval',
            field=models.BooleanField(default=False, verbose_name='تایید مدیریت'),
        ),
        migrations.AddField(
            model_name='repair_request',
            name='Molding_office_approval',
            field=models.BooleanField(default=False, verbose_name='تایید دفتر قالبسازی'),
        ),
        migrations.AddField(
            model_name='repair_request',
            name='QC_approval',
            field=models.BooleanField(default=False, verbose_name='تایید مدیریت کیفیت و تولید'),
        ),
    ]
