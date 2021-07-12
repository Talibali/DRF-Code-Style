from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            info = Student.objects.get(id=id)
            serializer = StudentSerializer(info)
            return Response(serializer.data)

        info = Student.objects.all()
        serializer = StudentSerializer(info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = StudentSerializer(data=request.data)
        if(data.is_valid()):
            data.save()
            return Response({'msg':'Data created!'}, status=status.HTTP_201_CREATED)
        return Response(data.errors)

    if request.method == 'PUT':
        id = pk
        details = Student.objects.get(id=id)
        data = StudentSerializer(details, data=request.data)
        if(data.is_valid()):
            data.save()
            return Response({'msg':'Data Updated successfully!'}, status=status.HTTP_200_OK)
        return Response(data.errors)

    if request.method == 'DELETE':
        id = pk
        details = Student.objects.get(id=id)
        data = details.delete()
        if data:
            return Response({'msg':'Data Delete successfully!'}, status=status.HTTP_204_NO_CONTENT)
        return Response(data.errors)


