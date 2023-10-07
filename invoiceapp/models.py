import uuid
from django.db import models

# Create your models here.
# myapp/models.py
from django.db import models

class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    customer_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class InvoiceDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='details')
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unite_price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return str(self.id)
