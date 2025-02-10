from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from rest_framework.exceptions import NotFound, ParseError
from .models import ToDo
from .serializers import ToDoSerializer

class ToDoAPIView(APIView):

    # GET ALL
    def get(self, request):
        try:
            todos = ToDo.objects.all()
            serializer = ToDoSerializer(todos, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # GET BY ID METHOD (MENCEGAH PENULISAN BERULANG QUERY)
    def get_object(self, pk):
        try:
            return ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            raise NotFound(detail="Data tidak ditemukan", code=status.HTTP_404_NOT_FOUND)

    #
    def get(self, request, pk=None):
        if pk is not None:
            try:
                todo = self.get_object(pk)
                serializer = ToDoSerializer(todo)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            except NotFound as e:
                return Response({"status": "error", "message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        return self.get(request)  # Jika tanpa pk, kembalikan semua data

    # POST (CREATE)
    def post(self, request):
        try:
            serializer = ToDoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)  # Akan otomatis raise ValidationError jika data tidak valid
            serializer.save()
            return Response({"status": "success", "message": "Data berhasil dibuat", "data": serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"status": "error", "message": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # PATCH (UPDATE PARTIAL)
    def patch(self, request, pk):
        try:
            todo = self.get_object(pk)
            serializer = ToDoSerializer(todo, data=request.data, partial=True)  # partial=True untuk update sebagian
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"status": "success", "message": "Data berhasil diperbarui", "data": serializer.data}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"status": "error", "message": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except NotFound as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # DELETE
    def delete(self, request, pk):
        try:
            todo = self.get_object(pk)
            todo.delete()
            return Response({"status": "success", "message": "Data berhasil dihapus"}, status=status.HTTP_204_NO_CONTENT)
        except NotFound as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
