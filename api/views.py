from django.shortcuts import render
from rest_framework import  status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Page
from .serializers import PageSerializers

@api_view(['GET','POST'])
def page_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Page.objects.get(id=id)
            serializer = PageSerializers(stu)
            return Response(serializer.data)
        stu = Page.objects.all()
        serializer = PageSerializers(stu,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PageSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)