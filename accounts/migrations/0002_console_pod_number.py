# Generated by Django 3.1.6 on 2021-02-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='console',
            name='pod_number',
            field=models.IntegerField(default=0),
        ),
    ]
