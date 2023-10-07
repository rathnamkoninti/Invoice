# invoices/serializers.py

from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = "__all__"

class InvoiceSerializer(serializers.ModelSerializer):
    invoice_details = InvoiceDetailSerializer(many=True, required=False)

    class Meta:
        model = Invoice
        fields = ['id', 'date', 'customer_name', 'invoice_details']

    def create(self, validated_data):
        print(validated_data)  # Add this line for debugging
        invoice_details_data = validated_data.pop('invoice_details', [])
        invoice = Invoice.objects.create(**validated_data)

        for detail_data in invoice_details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)

        return invoice

