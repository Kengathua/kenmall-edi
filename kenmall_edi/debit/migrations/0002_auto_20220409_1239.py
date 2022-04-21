# Generated by Django 3.2.12 on 2022-04-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='units',
            name='section',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='units',
            name='category',
        ),
        migrations.AddField(
            model_name='units',
            name='category',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
