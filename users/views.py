from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .models import CustomUser

class UserRegistrationView(APIView):

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({ "message":"Usuario Registrado Exitosamente",
                'token': token.key,
                'user_id': user.id,
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ValidateRegisterView(APIView):
    
    def get(self,request):
     constrains={
            'first_name': {
                'min_length': 3,
                'max_length': CustomUser._meta.get_field('first_name').max_length,
            },
            'last_name': {
                'min_length': 3,
                'max_length': CustomUser._meta.get_field('last_name').max_length,
            },
            'email': {
                'min_length': 3,
                'max_length': 40,
                'unique': True,
                'validators': ['El email debe contener "@".'],
            },
            'password': {
                'max_length': 25,
                'validators': [
                    'La contraseña debe tener al menos 8 caracteres.',
                    'La contraseña debe contener al menos 2 números.'
                ],
            },
            'phone_number': {
                'max_length': 8,
                'regex': r'^\d{8}$',
                'message': "El número debe contener 8 dígitos.",
                'required': False,
            },
        }
     return Response(constrains)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user_id': user.id,
                    'email': user.email
                })
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Sesión cerrada exitosamente.'}, status=status.HTTP_200_OK)
        except AttributeError:
            return Response({'error': 'Usuario no autenticado.'}, status=status.HTTP_400_BAD_REQUEST)