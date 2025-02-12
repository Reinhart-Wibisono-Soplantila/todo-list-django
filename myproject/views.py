from dj_rest_auth.views import LogoutView as DefaultLogoutView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

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