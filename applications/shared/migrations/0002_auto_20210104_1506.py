# Generated by Django 3.1.2 on 2021-01-04 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='color',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='display',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='icon',
            field=models.CharField(max_length=50, null=True),
        ),
    ]