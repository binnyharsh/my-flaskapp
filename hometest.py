import unittest

from homepage import app

class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.data, )
    
    def test_other(self):
        tester = app.test.client(self)
        response = tester.get('a', content_type='html/text')
        self.assertEqual(response.status_code, 404)
        self.assertTrue(b'Does NOT Exist !' in response.data)

if __name__ == '__main__':
    unittest.main()
