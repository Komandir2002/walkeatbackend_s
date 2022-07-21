from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserRegisterSerializer, LoginSerializer

from rest_framework.decorators import APIView


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)

        # data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"status": "User register successfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            data = serializer.errors
            return Response(data)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    # renderer_classes = (UserJSONRenderer,)
    def post(self, request):
        data = {"error": status.HTTP_400_BAD_REQUEST}
        user = request.data.get("user", {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data)
