# Generated by Django 2.0.5 on 2018-07-24 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoblog', '0002_auto_20180724_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipadress',
            name='ip_adress',
            field=models.TextField(null=True),
        ),
    ]