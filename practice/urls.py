from django.contrib import admin
from django.urls import path, include
from user import views
from authTokenAPI.auth import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee', views.EmployeeModule.as_view()),
    path('employees/', views.getEmployees),
    path('student/', include('functionAPIview.urls')),
    path('department/', include('classAPIview.urls')),
    path('gettoken', CustomAuthToken.as_view()) # To Create token by end user

]
