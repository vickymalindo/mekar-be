from rest_framework import serializers
from .models import Account
class AccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account
    fields = ['id', 'name', 'identity_number', 'email', 'date_of_birth']