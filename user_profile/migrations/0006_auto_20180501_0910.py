# Generated by Django 2.0.3 on 2018-05-01 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20180501_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='salutation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_profile.Salutation'),
        ),
    ]
