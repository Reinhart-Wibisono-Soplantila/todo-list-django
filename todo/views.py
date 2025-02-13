from django.shortcuts import render

#viewset 
from rest_framework import viewsets

# APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

#Error Handling
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound, ValidationError

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
        try:
            # todo_by_user=ToDo.objects.filter(user=request.user)
            # status=request.query_params.get('status')
            # if status:
            #     todos=todo_by_user.filter(status=status)
            
            # date=request.query_params.get('created_at')
            # if date:
            #     todos=todo_by_user.filter(created_at__date=date)
            
            # search=request.query_params.get('search')
            # if search:
            #     todos=todo_by_user.filter(title__icontains=search)|todo_by_user.filter(description__icontains=search)
            
            # serializer=ToDoSerializers(todos, many=True)
            # return Response({
            #     "status_code":status.HTTP_200_OK,
            #     "status":"success",
            #     "message":"Successfully retireved all data",
            #     "data":serializer.data
            # }, status=status.HTTP_200_OK)    
                
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
        
        except Exception as e:
            return Response({
                "status_code":status.HTTP_500_INTERNAL_SERVER_ERROR,
                "status":"error",
                "message":"Internal Server Error: " + str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
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
        
        except ValidationError as e:
            return Response({
                "status_code":status.HTTP_400_BAD_REQUEST,
                "status":"error",
                "message":str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                "status_code":status.HTTP_500_INTERNAL_SERVER_ERROR,
                "status":"error",
                "message":"Internal Server Error: " + str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # PUT & PATCH
    # Tanpa Partial (Mengupdate semua data)
    def put(self, request, todo_id):
        try:
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
            
            return Response({
                "status_code":status.HTTP_400_BAD_REQUEST,
                "status":"error",
                "message":str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "status_code":status.HTTP_500_INTERNAL_SERVER_ERROR,
                "status":"error",
                "message":"Internal Server Error: "+ str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # Menggunakan Partial (Mengupdate data yang hanya diubah)
    def patch(self, request, todo_id):
        try:
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
            return Response({
                "status_code":status.HTTP_400_BAD_REQUEST,
                "status":"error",
                "message":str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                "status_code":status.HTTP_500_INTERNAL_SERVER_ERROR,
                "status":"error",
                "message":"Internal Server Error: "+str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, todo_id):
        try:
            todo_object=get_object_or_404(ToDo, id=todo_id)
            todo_object.delete()
            return Response({
                "status_code":status.HTTP_204_NO_CONTENT,
                "status":"success",
                "message":"successfully delete data"
            }, status=status.HTTP_204_NO_CONTENT)
            
        except Exception as e:
            return Response({
                "status_code":status.HTTP_500_INTERNAL_SERVER_ERROR,
                "status":"error",
                "message":"Internal Server Error: "+str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def options(self, request, *args, **kwargs):
        return Response({
            "status_code":status.HTTP_200_OK,
            "status":"success",
            "allow":["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
            "message":"These are the allowed methods for this endpoint."
        })