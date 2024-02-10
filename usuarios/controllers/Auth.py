from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Puedes agregar campos adicionales al token si lo deseas
    # Aquí se muestra un ejemplo de cómo agregar el nombre de usuario al token
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        # Puedes agregar más campos si lo deseas
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    # Puedes personalizar la respuesta de la vista si lo deseas
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Realiza alguna acción adicional si lo deseas
            # Aquí se muestra cómo obtener el token
            token = serializer.validated_data
            return Response({
                'token': token['access'],
                'refresh_token': token['refresh'],
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
