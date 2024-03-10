from django.shortcuts import render
from exuser.models import Nuser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from exuser.serializers import *

# Create your views here.

@api_view(['GET'])
def employee(request):
	nuser = Nuser.objects.all()
	nuserserializer = NuserSerializer(nuser, many=True)
	return Response(nuserserializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addemployee(request):
	password = request.data.get('password')
	request.data['password'] = make_password(password)
	nuserserializer = NuserSerializer(data=request.data, many=False)
	if nuserserializer.is_valid():
		nuserserializer.save()
		return Response(nuserserializer.data, status=status.HTTP_200_OK)
	else:
		return Response(nuserserializer.errors, status=status.HTTP_400_BAD_REQUEST)
