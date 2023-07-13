from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Professor, Student


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    USER_TYPES = (
        ('professor', 'Professor'),
        ('student', 'Student')
    )

    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    user_type = serializers.ChoiceField(choices=USER_TYPES, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'phone_number',
                  'date_of_birth', 'image', 'gender', 'created_at', 'updated_at', 'address', 'country', 'city',
                  'user_type')

        extra_kwargs = {'password': {'write_only': True},
                        'confirm_password': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password', None)
        if password != confirm_password:
            raise serializers.ValidationError('Passwords do not match')
        return data

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        password = validated_data.pop('password')
        user = get_user_model().objects.create(**validated_data)
        user.set_password(password)
        if user_type.lower() == 'professor':
            Professor.objects.create(user=user)
        elif user_type.lower() == 'student':
            Student.objects.create(user=user)
        else:
            raise serializers.ValidationError('Invalid user type')
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        if password and confirm_password and password != confirm_password:
            raise serializers.ValidationError('Passwords do not match')
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance