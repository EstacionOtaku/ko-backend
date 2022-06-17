from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, RegisterSerializer


# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        # ejecutar el validador
        serializer.is_valid(raise_exception=True)
        # ejecutar la acción (guardado, actualización, eliminación)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
