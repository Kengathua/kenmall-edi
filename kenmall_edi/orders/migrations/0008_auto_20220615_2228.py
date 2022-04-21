# Generated by Django 3.2.12 on 2022-06-15 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20220615_2209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='purchase_order_date',
            new_name='order_date',
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('PROCESSING', 'PROCESSING'), ('CANCELLED', 'CANCELLED'), ('FULFILLED', 'FULFILLED')], default='PENDING', max_length=300),
        ),
    ]
