# Generated by Django 4.2.5 on 2024-01-30 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_continuousassessment_courseattendance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseattendance',
            name='comment',
        ),
        migrations.AddField(
            model_name='continuousassessment',
            name='comment',
            field=models.TextField(default=' '),
        ),
    ]
