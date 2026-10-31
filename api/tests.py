from rest_framework.test import APITestCase

class ApiTests(APITestCase):
    def test_health(self):
        r = self.client.get("/api/health/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), {"status": "ok"})

    def test_hello(self):
        r = self.client.get("/api/hello/")
        self.assertEqual(r.status_code, 200)
        self.assertIn("message", r.json())

    def test_hello_has_author(self):
        r = self.client.get("/api/hello/")
        self.assertEqual(r.json()["author"], "Oguz")