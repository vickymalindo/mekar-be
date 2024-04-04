from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
  def setUp(self):
    self.insert_account = reverse('account')

    self.empty_data = {
      "name": "",
      "identity_number": "",
      "email": "",
      "date_of_birth": ""
    }

    self.account_data = {
      "name": "epson",
      "identity_number": "3151684651131",
      "email": "ep@gmail.com",
      "date_of_birth": "2024-12-03"
    }

    self.email_more_than_capacity = {
      "name": "golang",
      "identity_number": "3151684651131",
      "email": "golang@gmail.com",
      "date_of_birth": "2024-12-03"
    }

    self.identity_more_than_capacity = {
      "name": "saiful",
      "identity_number": "31516846511000031",
      "email": "sl@gmail.com",
      "date_of_birth": "2024-12-03"
    }

    return super().setUp()
  
  def tearDown(self):
    return super().tearDown()
