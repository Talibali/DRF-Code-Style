from rest_framework import serializers
from django.core.validators import RegexValidator
from common.constants import ConstantMessages
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    ''' Regular Serializer concept'''
    # id = serializers.IntegerField()
    # name = serializers.CharField(max_length=50)
    # email = serializers.EmailField(max_length=50)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=ConstantMessages.PHONE_MESSAGE)
    # phone = serializers.CharField(validators=[phone_regex], max_length=10)
    # marital_status = serializers.BooleanField(default=False)
    # dob = serializers.DateField()

    '''Create and update method will use if we are using regular serializer to create and update record'''
    # def create(self, validated_data):
    #     return Employee.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.marital_status = validated_data.get('marital_status', instance.marital_status)
    #     instance.dob = validated_data.get('dob', instance.dob)
    #     instance.save()
    #     return instance

    '''Name - Field validation'''
    def validate_name(self, value):
        if value == 'Talib':
            raise serializers.ValidationError("Already name exist")
        return value