from .test_setup import TestSetUp

class TestViews(TestSetUp):
  def test_empty_data(self):
    res = self.client.post(self.insert_account, self.empty_data, format="json")
    self.assertEqual(res.status_code, 404)
  
  def test_with_data(self):
    res = self.client.post(self.insert_account, self.account_data, format="json")
    self.assertEqual(res.status_code, 201)

  def test_email_more_than_capacity(self):
    res = self.client.post(self.insert_account, self.email_more_than_capacity, format="json")
    self.assertEqual(res.status_code, 404)

  def test_identity_more_than_capacity(self):
    res = self.client.post(self.insert_account, self.identity_more_than_capacity, format="json")
    self.assertEqual(res.status_code, 404)


