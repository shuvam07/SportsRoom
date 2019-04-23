from django.test import TestCase,SimpleTestCase

# Create your tests here.
class TestUrls(SimpleTestCase):
	
	def test_home_url_is_resolved(self):
		assert 1==2