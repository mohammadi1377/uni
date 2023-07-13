from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import Professor, User, Student


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        print('/////////////////////////')
        # check if user type is provided in request data
        user_type = request.data.get('user_type', None)
        print(user_type,'*-*-*-*-*-*-*-*-*-*')
        if user_type is None:
            return Response({"error": "User type is required"}, status=status.HTTP_400_BAD_REQUEST)

        # validate and save user data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer,'****************')
        user = serializer.save()

        # create corresponding Professor or Student object based on user type
        if user_type.lower() == 'professor':
            Professor.objects.create(user=user)
        elif user_type.lower() == 'student':
            Student.objects.create(user=user)
        else:
            return Response({"error": "Invalid user type"}, status=status.HTTP_400_BAD_REQUEST)

        response_data = {
            "success": True,
            "message": "User registered successfully",
            "data": serializer.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
