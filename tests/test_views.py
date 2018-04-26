import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from tutorial.views import TutorialViews

        request = testing.DummyRequest()
        inst = TutorialViews(request)
        response = inst.home()
        self.assertEqual(response.status, '302 Found')

    def test_plain_without_name(self):
        from tutorial.views import TutorialViews

        request = testing.DummyRequest()
        inst = TutorialViews(request)
        response = inst.plain()
        self.assertIn(b'No Name Provided', response.body)

    def test_plain_with_name(self):
        from tutorial.views import TutorialViews

        request = testing.DummyRequest()
        request.GET['name'] = 'Jane Doe'
        inst = TutorialViews(request)
        response = inst.plain()
        self.assertIn(b'Jane Doe', response.body)
