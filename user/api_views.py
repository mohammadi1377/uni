from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer, StudentSerializer, ProfessorSerializer, LoginSerializer
from .models import Professor, User, Student
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
import logging

logger = logging.getLogger(__name__)


class RegisterView(generics.CreateAPIView):
	serializer_class = UserSerializer

	def create(self, request, *args, **kwargs):
		logger.debug("RegisterView - create method called")

		user_type = request.data.get('user_type', None)
		if user_type is None:
			logger.error("RegisterView - User type is required")
			return Response({"error": "User type is required"}, status=status.HTTP_400_BAD_REQUEST)

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()

		if user_type.lower() == 'professor':
			professor, _ = Professor.objects.get_or_create(user=user)
		elif user_type.lower() == 'student':
			student, _ = Student.objects.get_or_create(user=user)
		else:
			logger.error("RegisterView - Invalid user type")
			return Response({"error": "Invalid user type"}, status=status.HTTP_400_BAD_REQUEST)

		response_data = {
			"success": True,
			"message": "User registered successfully",
			"data": serializer.data
		}
		return Response(response_data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
	serializer_class = LoginSerializer

	def post(self, request, *args, **kwargs):
		logger.debug("LoginView - post method called")

		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		login(request, user)

		return Response({"success": True, "message": "User logged in successfully"})


class LogoutView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request, *args, **kwargs):
		logger.debug("LogoutView - post method called")

		logout(request)
		return Response({"success": True, "message": "User logged out successfully"})


class UserDetailView(APIView):
	permission_classes = [IsAuthenticated]
	serializer_class = UserSerializer

	def get(self, request, *args, **kwargs):
		logger.debug("UserDetailView - get method called")

		user = request.user
		serializer = self.serializer_class(user)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, *args, **kwargs):
		logger.debug("UserDetailView - put method called")

		user = request.user
		serializer = self.serializer_class(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, *args, **kwargs):
		logger.debug("UserDetailView - delete method called")

		user = request.user
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class StudentDetailView(APIView):
	permission_classes = [IsAuthenticated]
	serializer_class = StudentSerializer

	def get(self, request, *args, **kwargs):
		logger.debug("StudentDetailView - get method called")

		student = Student.objects.filter(user=request.user).first()
		if not student:
			logger.error("StudentDetailView - Student not found.")
			raise ValueError("Student not found.")
		serializer = self.serializer_class(student)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, *args, **kwargs):
		logger.debug("StudentDetailView - put method called")

		student = Student.objects.filter(user=request.user).first()
		if not student:
			logger.error("StudentDetailView - Student not found.")
			raise ValueError("Student not found.")
		serializer = self.serializer_class(student, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, *args, **kwargs):
		logger.debug("StudentDetailView - delete method called")

		student = Student.objects.filter(user=request.user).first()
		if not student:
			logger.error("StudentDetailView - Student not found.")
			raise ValueError("Student not found.")
		student.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class ProfessorDetailView(APIView):
	permission_classes = [IsAuthenticated]
	serializer_class = ProfessorSerializer

	def get(self, request, *args, **kwargs):
		logger.debug("ProfessorDetailView - get method called")

		professor = Professor.objects.filter(user=request.user).first()
		if not professor:
			logger.error("ProfessorDetailView - Professor not found.")
			raise ValueError("Professor not found.")
		serializer = self.serializer_class(professor)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, *args, **kwargs):
		logger.debug("ProfessorDetailView - put method called")

		professor = Professor.objects.filter(user=request.user).first()
		if not professor:
			logger.error("ProfessorDetailView - Professor not found.")
			raise ValueError("Professor not found.")
		serializer = self.serializer_class(professor, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, *args, **kwargs):
		logger.debug("ProfessorDetailView - delete method called")

		professor = Professor.objects.filter(user=request.user).first()
		if not professor:
			logger.error("ProfessorDetailView - Professor not found.")
			raise ValueError("Professor not found.")
		professor.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
