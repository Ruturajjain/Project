# Generated by Django 3.0 on 2022-03-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moverspackers', '0002_auto_20220301_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='shiftingdate',
            field=models.DateField(max_length=200, null=True),
        ),
    ]
