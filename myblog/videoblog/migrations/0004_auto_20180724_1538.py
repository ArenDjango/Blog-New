# Generated by Django 2.0.5 on 2018-07-24 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoblog', '0003_auto_20180724_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipadress',
            name='ip_adress',
            field=models.GenericIPAddressField(default=1),
            preserve_default=False,
        ),
    ]
