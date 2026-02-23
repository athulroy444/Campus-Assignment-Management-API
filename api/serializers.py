from rest_framework import serializers
from .models import Student, Assignment

class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'password', 'department', 'year']

    def create(self, validated_data):
        student = Student.objects.create_user(
            username=validated_data['email'], # Use email as username
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data.get('name', ''),
            department=validated_data.get('department', ''),
            year=validated_data.get('year', None)
        )
        return student

class AssignmentSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.email')

    class Meta:
        model = Assignment
        fields = ['id', 'student', 'title', 'description', 'subject', 'status', 'created_at']
        read_only_fields = ['created_at', 'student']
