# Generated by Django 3.2.12 on 2022-04-09 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debit', '0002_auto_20220409_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='units',
            options={'ordering': ['-created_on', '-units_name']},
        ),
    ]
