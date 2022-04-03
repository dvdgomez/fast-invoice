import os
import unittest

from fastapi.testclient import TestClient

from .main import app


# Tests numbered to enforce order to check expected states of database
class TestInvoiceApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test01_read_main(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Not Found"})

    def test02_read_empty_invoices(self):
        response = self.client.get("/invoices/")
        self.assertEqual(response.status_code, 200)
        # Should be empty, no invoices posted yet
        self.assertEqual(response.json(), [])

    def test03_create_invoice(self):
        # Invalid empty post results in error
        response = self.client.post("/invoices/", json={})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), {
                'detail': [{
                    'loc': ['body', 'date'], 'msg': 'field required', 'type': 'value_error.missing'
                    }]
                })

        # Valid post results in successful response
        response = self.client.post("/invoices/", json={
            "date": "2022-04-03"
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'date': '2022-04-03', 'id': 1, 'invoice_items': []})

    def test04_read_invoices(self):
        response = self.client.get("/invoices/")
        self.assertEqual(response.status_code, 200)
        # Response no longer empty, contains earlier invoice
        self.assertEqual(response.json(), [{'date': '2022-04-03', 'id': 1, 'invoice_items': []}])
        # Insert invoice then attempt read again, response should not be empty

    def test05_read_invoice(self):
        # Check invalid invoice
        response = self.client.get("/invoices/5/")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Invoice not found"})
        # Check valid invoice
        response = self.client.get("/invoices/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'date': '2022-04-03', 'id': 1, 'invoice_items': []})

    def test06_create_invoice_item(self):
        response = self.client.post("/invoices/1/invoice_items/", json={})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), {'detail': [{'loc': ['body', 'units'],
                      'msg': 'field required',
                      'type': 'value_error.missing'},
                     {'loc': ['body', 'amount'],
                      'msg': 'field required',
                      'type': 'value_error.missing'}]})
        # Check response of valid post
        response = self.client.post("/invoices/1/invoice_items/", json={
            "units": 0, "description": "test", "amount": 0
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'units': 0, 'description': 'test', 'amount': 0.0, 'id': 1, 'invoice_id': 1
            })

    def test07_read_invoice_items(self):
        response = self.client.get("/invoice_items/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{
            'amount': 0.0, 'description': 'test', 'id': 1, 'invoice_id': 1, 'units': 0
            }])

    @classmethod
    def tearDownClass(cls):
        # Remove test database file after testing concludes
        if os.path.isfile("invoice_app.db"):
            os.remove("invoice_app.db")


if __name__ == '__main__':
    unittest.main()
