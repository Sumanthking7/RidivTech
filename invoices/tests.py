from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(APITestCase):

    def setUp(self):
        self.invoice_data = {'date': '2022-01-01', 'customer_name': 'Test Customer'}
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.invoice_detail_data = {'invoice': self.invoice.id, 'description': 'Test Description',
                                    'quantity': 2, 'unit_price': 10.0, 'price': 20.0}
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)

    def test_create_invoice(self):
        url = reverse('invoice-list-create')
        response = self.client.post(url, self.invoice_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Invoice.objects.count(), 2)

