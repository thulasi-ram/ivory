# Generated by Django 2.0.3 on 2018-03-25 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_accounts', '0003_auto_20180325_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalentity',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='common.Address'),
        ),
    ]