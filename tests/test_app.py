import unittest
from app import create_app
import json
import pandas as pd

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"De-Anonymization Review Platform", response.data)

    def test_upload_and_assess_with_data_type(self):
        data = {
            "patient_id": [1, 2, 3],
            "diagnosis": ["Flu", "Cold", "Flu"]
        }
        df = pd.DataFrame(data)
        df.to_csv('test_ehr.csv', index=False)
        with open('test_ehr.csv', 'rb') as f:
            response = self.client.post('/upload', data={'file': f, 'dataType': 'ehr'})
            self.assertEqual(response.status_code, 200)
            result = json.loads(response.data)
            self.assertIn('data_type', result)
            self.assertEqual(result['data_type'], 'ehr')
            self.assertIn('risk_results', result)

    def test_upload_and_assess_without_data_type(self):
        data = {
            "patient_id": [1, 2, 3],
            "diagnosis": ["Flu", "Cold", "Flu"]
        }
        df = pd.DataFrame(data)
        df.to_csv('test_ehr.csv', index=False)
        with open('test_ehr.csv', 'rb') as f:
            response = self.client.post('/upload', data={'file': f})
            self.assertEqual(response.status_code, 200)
            result = json.loads(response.data)
            self.assertIn('data_type', result)
            self.assertEqual(result['data_type'], 'ehr')
            self.assertIn('risk_results', result)

if __name__ == "__main__":
    unittest.main()