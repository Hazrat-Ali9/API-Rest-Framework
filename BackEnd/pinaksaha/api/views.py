from django.shortcuts import render
from .models import DataStoreModel
from .serializers import DataStoreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DataList(APIView):
    def get(self, request, format=None):
        models = DataStoreModel.objects.all()
        serializer = DataStoreSerializer(models, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DataStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class DataUpdateDelete(APIView):
#    
    def get_object(self, pk):
        try:
            return DataStoreModel.objects.get(pk=pk)
        except DataStoreModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DataStoreSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DataStoreSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
