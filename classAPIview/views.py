from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import DepartmentSerializer
from .models import Department
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.filters import SearchFilter
# from rest_framework.pagination import PageNumberPagination
from .mypagination import MyPagination


# Create your views here.
# Practice about APIView
class departmen_api(APIView):

    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated] # Only registered user (superadmin /admin/normal user/) can access
    #permission_classes = [IsAdminUser]  # Only staff member and superadmin can access
    permission_classes = [AllowAny] # Any (authenticate or nonauthenticate) user can access

    def get(self, request, format=None, pk=None):
        if pk is not None:
            record = Department.objects.get(id=pk)
            serializer = DepartmentSerializer(record)
            return Response({"msg":"Get records", "data": serializer.data},  status=status.HTTP_200_OK)
        records = Department.objects.all()
        serializer = DepartmentSerializer(records, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Record created!!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None, pk=None):
        record = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(record, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Record updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def delete(self, request, format=None, pk=None):
        if pk is not None:
            record = Department.objects.get(id=pk)
            record.delete()
            return Response({'msg': 'Record Deleted successfully!!'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'msg': 'Not Found!!'}, status=status.HTTP_404_NOT_FOUND)


# Practice about Viewset
class DepartmentViewSet(viewsets.ViewSet):

    # authentication_classes = [BasicAuthentication] # For Basis Authentication i.e require user name and pw on popup
    # authentication_classes = [SessionAuthentication] # For user session check with user name and pw in window
    # authentication_classes = [TokenAuthentication] # For user can access API if they have valid token
    # permission_classes = [IsAuthenticated] # Only registered user (superadmin /admin/normal user/) can access
    # permission_classes = [IsAdminUser] # Only staff member and superadmin can access
    # permission_classes = [AllowAny] # Any (authenticate or nonauthenticate) user can access

    pagination_class = MyPagination

    def list(self, request):
        records = Department.objects.all()
        serializer = DepartmentSerializer(records, many=True)
        return Response(serializer.data)

    def retrieve(self, request, format=None, pk=None):
        if pk is not None:
            record = Department.objects.get(id=pk)
            serializer = DepartmentSerializer(record)
            return Response({"msg":"Get records", "data": serializer.data},  status=status.HTTP_200_OK)

    def create(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Record created!!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, format=None, pk=None):
        record = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(record, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Record updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def destroy(self, request, format=None, pk=None):
        if pk is not None:
            record = Department.objects.get(id=pk)
            record.delete()
            return Response({'msg': 'Record Deleted successfully!!'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'msg': 'Not Found!!'}, status=status.HTTP_404_NOT_FOUND)

# Practice about ModelViewSet

# class DepartmentModelView(viewsets.ModelViewSet):
#     records = Department.objects.all()
#     serializer = DepartmentSerializer()