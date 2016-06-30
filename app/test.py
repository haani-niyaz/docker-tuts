import unittest
import identidock

class TestCase(unittest.TestCase):
	
	# Initialize test version of our app
	def setUp(self):
		identidock.app.config["TESTING"] = True
		self.app = identidock.app.test_client()

	def test_get_main_page(self):
		page = self.app.post("/",data=dict(name='Moby Dock'))
		assert page.status_code == 200
		assert 'Moby Dock' in str(page.data)

	def test_html_escaping(self):
		page = self.app.post("/",data=dict(name='"><b>TEST</b><!--"'))
		assert '<b>' not in str(page.data)


if __name__ == '__main__':
	unittest.main()
