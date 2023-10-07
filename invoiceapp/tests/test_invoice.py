from django.test import tag
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from invoiceapp.models import Invoice


@tag("invoiceapp", "Invoice")
class ContactsTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice = Invoice.objects.create(
            date="2023-10-07",
            customer_name="nirmala",
        )

    def test_get_invoice_list_success(self):
        """invoice get api: all records"""
        url = reverse("invoice-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invoice_details_success(self):

        url = reverse("invoice-list-create")
        query_param_value = self.invoice.id
        response = self.client.get(f"{url}?id={query_param_value}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_invoice_create_success(self):
        """Create Invoice with valid data"""
        url = reverse("invoice-list-create")
        payload = {
            "date": "2023-10-06",
            "customer_name": "rktest",
        }
        response = self.client.post(url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["message"], "Invoice Created Successfully")

    def test_put_invoice_success(self):
        """Update Invoice with valid data"""
        url = reverse("invoice-list-create")
        payload = {
            "id": self.invoice.id,
           "date": "2023-10-06",
            "customer_name": "rktest Edit",
        }
        response = self.client.put(url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["message"], "Invoice Successfully Updated")

    def test_delete_enquiry_success(self):
        """
        invoice delete api: invoice delete
        """

        url = reverse("invoice-list-create")
        invoice_id = self.invoice.id
        response = self.client.delete(f"{url}?id={invoice_id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)