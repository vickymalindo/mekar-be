from  django.http import JsonResponse
from .models import Account
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def account_list(request):
  if request.method == 'GET':
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return JsonResponse({"accounts": serializer.data})
  
  if request.method == 'POST':
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)