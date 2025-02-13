from dj_rest_auth.views import LogoutView as DefaultLogoutView
from todo.serializers import RegistrationSerializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

    
# Registrasi
class RegisterView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer=RegistrationSerializers(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response({
                    "status_code":status.HTTP_201_CREATED,
                    "status":"success",
                    "message":"Successfully create data",
                    "data":serializer.data
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(DefaultLogoutView):
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
        try:
            refresh_token=request.data.get("refresh")
            if refresh_token:
                token=RefreshToken(refresh_token)
                token.blacklist()
            return super().post(request)
        except Exception as e:
            return Response({"error": "Token tidak valid"}, status=400)