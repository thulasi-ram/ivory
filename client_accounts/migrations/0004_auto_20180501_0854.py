# Generated by Django 2.0.3 on 2018-05-01 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_accounts', '0003_auto_20180501_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientaccount',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='legalentity',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
    ]