from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer, LoginSerializer

from rest_framework.decorators import APIView






class UserViewSet(ModelViewSet):
    permission_classes = [AllowAny,]
    serializer_class = UserSerializer
    queryset = User.objects.all()



class LoginAPIView(APIView):
    permission_classes = [AllowAny,]
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                username = serializer.data["phone"]
                password = serializer.data["password"]
                user = authenticate(username=username, password=password)
                if user is None:
                    data = "User not found"
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST, data={"status": data}
                    )

                refresh = RefreshToken.for_user(user)
                access = AccessToken.for_user(user)

                return Response(
                    {
                        "status": status.HTTP_200_OK,
                        "user": user.username,
                        "refresh": str(refresh),
                        "access": str(access),
                    }
                )
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)



