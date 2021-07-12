from django.shortcuts import render
from rest_framework.parsers import JSONParser
from user.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeModule(View):
    def get(self, request, *args, **kwargs):

        ''' Get Specific record'''

        json_data = request.body
        stream = io.BytesIO(json_data)
        parsedata = JSONParser().parse(stream)
        getId = parsedata.get('eid', None)

        if getId is not None:
            employee = Employee.objects.get(id=getId)
            serializer = EmployeeSerializer(employee)
            return JsonResponse(serializer.data, safe=False)
        employees = Employee.objects.all(many=True)
        serializer1 = EmployeeSerializer(employees)
        return JsonResponse(serializer1.data)

    def post(self, request, *args, **kwargs):

        ''' Create Specific record'''

        json_data = request.body
        stream = io.BytesIO(json_data)
        parseData = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=parseData)

        if serializer.is_valid():
            serializer.save()
            msg = {"response_msg": "Created successfully"}
            return JsonResponse(msg)
        else:
            return JsonResponse(serializer.errors)

    def put(self, request, *args, **kwargs):

        ''' Update Specific record'''

        json_data = request.body
        stream = io.BytesIO(json_data)
        parseData = JSONParser().parse(stream)
        getId = parseData.get('id')
        getData = Employee.objects.get(id=getId)
        serializer = EmployeeSerializer(getData, data=parseData)

        if serializer.is_valid():
            serializer.save()
            msg = {"response_msg": "Update successfully"}
            return JsonResponse(msg)
        else:
            return JsonResponse(serializer.errors)

    def delete(self, request, *args, **kwargs):

        ''' Delete Specific record'''

        json_data = request.body
        stream = io.BytesIO(json_data)
        parseData = JSONParser().parse(stream)
        getId = parseData.get('id')
        getData = Employee.objects.get(id=getId)

        delete_data = getData.delete()
        if delete_data:
            msg = {"response_msg": "Delete successfully"}
            return JsonResponse(msg)


# @csrf_exempt
# def getEmployee(request):
#
#     '''GET Specific employee details'''
#
#     if request.method == 'GET':
#
#
#     # employee = Employee.objects.get(id=pk)
#     # serializer = EmployeeSerializer(employee)
#     # print(employee)
#     # json_data = JSONRenderer.render(serializer.data)
#     # return HttpResponse(json_data, content_type="content_type/json")
#     # return JsonResponse(serializer.data, safe=False)
#
#     if request.method == 'POST':
#
#     if request.method == 'PUT':
#
#
#     if request.method == 'DELETE':



def getEmployees(request):

    '''Get employees'''

    employees = Employee.objects.all()
    searialize = EmployeeSerializer(employees, many=True)
    return JsonResponse(searialize.data, safe=False)