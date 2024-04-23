from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# from .models import CustomUser
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.validated_data
    #     token, created = Token.objects.get_or_create(user=user)
    #     return Response({'token': token.key})

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # Retrieve the user with the provided username
        print("Hello")
        try:
            user = User.objects.get(username=username)
            print("try")
            print(user)
        except User.DoesNotExist:
            print("except")
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the provided password matches the user's password
        if not user.check_password(password):
            print("invalid")
            print(password)
            return Response({'error': 'Invalid password.'}, status=status.HTTP_400_BAD_REQUEST)

        print(password)
        # token = Token.objects.create(user=user)
        token, created = Token.objects.get_or_create(user=user)
        print(token.key)
        return Response({'token': token.key})

class UserLogoutAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
