from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from django.http import Http404
from .models import *
from .serializer import *
from django.db.models import Q
# Create your views here.
class RetrieveUserView(APIView):

    def get(self, request):
        queryset = UserAccount.objects.filter(is_staff = False).all().order_by('-date_joined')
        serialized = UserSerializer(queryset, many=True)

        return Response(serialized.data)
    
class GetUser(APIView):
    def get(self,request, id):
        try:
            user = UserAccount.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)        
        except UserAccount.DoesNotExist:
            raise Http404
        
class ProfileUpdateView(APIView):
    def post(self, request ,id):
        user = UserAccount.objects.get(id=id)
        userData =  UserSerializer(instance=user, data=request.data, partial=True)
        if userData.is_valid():
            userData.save()
            return Response(userData.data, status=status.HTTP_200_OK)
        return Response(400)
    
class UserSearchView(APIView):
    def get(self, request):
        keyword = request.GET.get('query')
        print(keyword)
        users = UserAccount.objects.filter(Q(name__icontains = keyword) | Q(phonenumber__icontains = keyword) , is_staff = False)
        serialized = UserSerializer(users, many=True)
        return Response(serialized.data)