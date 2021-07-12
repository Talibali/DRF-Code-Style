from django.urls import path, include
from functionAPIview import views

urlpatterns = [
    path('details', views.student_api),
    path('details/<int:pk>', views.student_api),

]