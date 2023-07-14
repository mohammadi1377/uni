from django.db import models


class Department(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Course(models.Model):
	name = models.CharField(max_length=200, help_text='Enter the name of the course')
	code = models.CharField(max_length=20, unique=True, help_text='Enter the course code')
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	description = models.TextField(help_text='Enter a brief description of the course')

	def __str__(self):
		return self.name


class Room(models.Model):
	name = models.CharField(max_length=50, help_text='Enter the room name or number')
	capacity = models.PositiveIntegerField(help_text='Enter the maximum number of occupants for the room')

	def __str__(self):
		return self.name


class Class(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	start_time = models.DateTimeField(help_text='Enter the start time of the class')
	end_time = models.DateTimeField(help_text='Enter the end time of the class')
	days_of_week = models.CharField(max_length=10, help_text='Enter the days of the week the class meets')

	def __str__(self):
		return f'{self.course} in {self.room} on {self.days_of_week}'


class Field(models.Model):
	name = models.CharField(max_length=100)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	description = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Specialization(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	field = models.ForeignKey(Field, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
