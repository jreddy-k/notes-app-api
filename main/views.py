from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import NotesSerializer
from .models import NotesModel
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class NotesList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = NotesModel.objects.all().reverse()
        serializer = NotesSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class NotesDetail(APIView):
    def get_object(self, pk):
        try:
            return NotesModel.objects.get(pk=pk)
        except NotesModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        NotesModel = self.get_object(pk)
        serializer = NotesSerializer(NotesModel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        NotesModel = self.get_object(pk)
        serializer = NotesSerializer(NotesModel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        NotesModel = self.get_object(pk)
        NotesModel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)