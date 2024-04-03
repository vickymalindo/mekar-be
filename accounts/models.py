from  django.db import models

class Account(models.Model):
  name = models.CharField(max_length=255)
  identity_number = models.CharField(max_length=16)
  email = models.CharField(max_length=15)
  date_of_birth = models.DateField()

  def __str__(self):
    return self.name + '_' + str(self.date_of_birth)