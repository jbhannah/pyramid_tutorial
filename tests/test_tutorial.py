import unittest


class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        from webtest import TestApp

        app = main({})
        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'Hi Home View', res.body)

    def test_hello(self):
        res = self.testapp.get('/howdy', status=200)
        self.assertIn(b'Hi Hello View', res.body)
