from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # department = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['name','email','phone','department']

    def __str__(self):
        return self.name
