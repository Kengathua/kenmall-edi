# Generated by Django 3.2.12 on 2022-06-15 19:09

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20220408_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrderItem',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False)),
                ('created_by', models.UUIDField(editable=False)),
                ('updated_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField()),
                ('enterprise', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='product_name',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='billing_address_id',
            new_name='guid',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='purchase_order_number',
            new_name='order_number',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='description',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='purchase_order_owner',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='quantity_in_stock',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='shipping_address_id',
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='customer_kenmall_code',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='sales_person',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='vendor_kenmall_code',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='carrier',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='contact_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='excise_duty',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='list_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='purchase_order_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='requisition_no',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='sales_commission',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='subject',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='terms_and_conditions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='tracking_number',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]