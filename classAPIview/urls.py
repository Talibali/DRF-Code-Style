from django.urls import path, include
from classAPIview import views
from rest_framework.routers import DefaultRouter

# Creating router object
router = DefaultRouter()

# Register DepartmentViewSet with router -> Definition:  As like Resource controller use Viewset
router.register('departmentviewSetapi', views.DepartmentViewSet, basename="department")

# Make Only three lines for CRUD use Model Viewset
# router.register('departmentmodelviewsetapi', views.DepartmentModelView, basename="department")

urlpatterns = [
    path('details', views.departmen_api.as_view()),
    path('details/<int:pk>', views.departmen_api.as_view()),

    # o/p for viewSet listing-> http://127.0.0.1:8000/department/departmentviewSetapi/
    path('', include(router.urls)),

    # for SessionAuthentication
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]