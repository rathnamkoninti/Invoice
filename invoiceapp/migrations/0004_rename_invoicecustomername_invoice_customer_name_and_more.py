# Generated by Django 4.2.6 on 2023-10-07 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0003_rename_date_invoice_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='InvoiceCustomerName',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='invoicedetail',
            old_name='unit_price',
            new_name='unite_price',
        ),
    ]
