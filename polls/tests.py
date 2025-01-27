from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from django.test import StaticLiveServerTestCase
from django.contrib.auth.models import User

class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument('--headless')
        cls.selenium = WebDriver(options=options)
        cls.selenium.implicitly_wait(5)

        # Crear superusuario
        user = User.objects.create_user("isard", "isard@isardvdi.com", "pirineus")
        user.is_superuser = True
        user.is_staff = True
        user.save()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_example(self):
        self.selenium.get(f'{self.live_server_url}/admin')
        assert "Django administration" in self.selenium.title
