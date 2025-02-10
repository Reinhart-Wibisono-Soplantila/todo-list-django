from django.shortcuts import render

#viewset 
from rest_framework import viewsets

# APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from .models import ToDo
from .serializers import ToDoSerializers

# Create your views here.

# Penggunaan Viewset
class ToDoViewSet(viewsets.ModelViewSet):
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializers
    

# Penggunaan APIView
class ToDoAPIView(APIView):
    def get(self, request, todo_id=None):
        
        # Get Specific 
        if todo_id:
            todo_object=get_object_or_404(ToDo, id=todo_id)
            serializer=ToDoSerializers(todo_object)
            return Response({
                "status_code":status.HTTP_200_OK,
                "status":"success",
                "message":"Successfully retireved specific data",
                "data":serializer.data
            }, status=status.HTTP_200_OK)
        
        # Get All
        todo_object=ToDo.objects.all()
        serializer=ToDoSerializers(todo_object, many=True)
        return Response({
            "status_code":status.HTTP_200_OK,
            "status":"success",
            "message":"Successfully retireved all data",
            "data":serializer.data
        }, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer=ToDoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status_code":status.HTTP_201_CREATED,
                "status":"success",
                "message":"Successfully create data",
                "data":serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # PUT & PATCH
    # Tanpa Partial (Mengupdate semua data)
    def put(self, request, todo_id):
        todo_object=get_object_or_404(ToDo, id=todo_id)
        serializer=ToDoSerializers(todo_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status_code":status.HTTP_200_OK,
                "status":"success",
                "message":"successfully update data",
                "data":serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Menggunakan Partial (Mengupdate data yang hanya diubah)
    def patch(self, request, todo_id):
        todo_object=get_object_or_404(ToDo, id=todo_id)
        serializer=ToDoSerializers(todo_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status_code":status.HTTP_200_OK,
                "status":"success",
                "message":"successfully update data",
                "data":serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, todo_id):
        todo_object=get_object_or_404(ToDo, id=todo_id)
        todo_object.delete()
        return Response({
            "status_code":status.HTTP_204_NO_CONTENT,
            "status":"success",
            "message":"successfully delete data"
        }, status=status.HTTP_204_NO_CONTENT)
        
    def options(self, request, *args, **kwargs):
        return Response({
            "status_code":status.HTTP_200_OK,
            "status":"success",
            "allow":["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
            "message":"These are the allowed methods for this endpoint."
        })