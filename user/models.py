from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from academic.models import Class, Department, Field, Specialization


class User(AbstractUser):
	phone_regex = RegexValidator(regex=r'09(\d{9})$',
								 message='Enter a valid mobile number. This value may contain only numbers.')
	phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)
	date_of_birth = models.DateField(default=timezone.now)
	image = models.ImageField(upload_to='media', blank=True, null=True)
	GENDER_CHOICES = [("male", "Male"), ("female", "Female")]
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
	address = models.TextField(blank=True)
	country = models.CharField(max_length=100, default='Iran')
	city = models.CharField(max_length=100, default='non')
	specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)

	@property
	def is_student(self):
		return hasattr(self, 'student')

	@property
	def is_teacher(self):
		return hasattr(self, 'professor')


class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	classes = models.ManyToManyField(Class)
	field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True)
	specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)

	class Meta:
		ordering = ["user__last_name", "user__first_name"]

	def __str__(self):
		return self.user.get_full_name()


class Professor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True)
	classes = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
	specializations = models.ManyToManyField(Specialization)

	def __str__(self):
		return self.user.get_full_name()
