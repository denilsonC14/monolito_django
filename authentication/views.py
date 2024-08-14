from datetime import datetime
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer, LoginSerializer
from .models import User
from rest_framework import status
from django.db import IntegrityError
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TareaEscolar
from .serializers import TareaEscolarSerializer
from .utils import es_dia_festivo

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"error": "Un usuario con ese nombre de usuario o correo electrónico ya existe"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class TareaEscolarViewSet(viewsets.ModelViewSet):
    serializer_class = TareaEscolarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TareaEscolar.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        fecha_entrega = serializer.validated_data['fecha_entrega']
        es_festivo, nombre_festivo = es_dia_festivo(fecha_entrega)
        
        if es_festivo:
            serializer.save(
                usuario=self.request.user,
                descripcion=f"{serializer.validated_data['descripcion']}\n\nADVERTENCIA: La fecha de entrega coincide con el día festivo: {nombre_festivo}"
            )
        else:
            serializer.save(usuario=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        response_data = serializer.data
        fecha_entrega = datetime.strptime(response_data['fecha_entrega'], '%Y-%m-%d').date()
        es_festivo, nombre_festivo = es_dia_festivo(fecha_entrega)
        
        if es_festivo:
            response_data['advertencia'] = f"La fecha de entrega coincide con el día festivo: {nombre_festivo}"
        
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)