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
    return Response({"status": "success", "message": "Get accounts success", "accounts": serializer.data})
  
  if request.method == 'POST':
    print(request.data)
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"status": "success", "message": "Insert account success", "account": serializer.data}, status=status.HTTP_201_CREATED)
    else:
      return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_404_NOT_FOUND)