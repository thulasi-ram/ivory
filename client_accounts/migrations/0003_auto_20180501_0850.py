# Generated by Django 2.0.3 on 2018-05-01 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_accounts', '0002_auto_20180501_0830'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('titlte', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='legalentity',
            name='business_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client_accounts.BusinessType'),
        ),
    ]
