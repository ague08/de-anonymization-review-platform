import unittest
from app import create_app
import json

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"De-Anonymization Review Platform", response.data)

    def test_upload_and_assess(self):
        data = {
            "age": [25, 34, 45, 52, 36],
            "gender": ["M", "F", "M", "F", "M"],
            "zip_code": [12345, 12345, 12345, 67890, 67890],
            "disease": ["Flu", "Cold", "Flu", "Cancer", "Flu"]
        }
        df = pd.DataFrame(data)
        df.to_csv('test.csv', index=False)
        with open('test.csv', 'rb') as f:
            response = self.client.post('/upload', data={'file': f})
            self.assertEqual(response.status_code, 200)
            result = json.loads(response.data)
            self.assertIn('k_anonymity', result)
            self.assertIn('l_diversity', result)
            self.assertIn('t_closeness', result)

if __name__ == "__main__":
    unittest.main()