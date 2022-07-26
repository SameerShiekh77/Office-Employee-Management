from rest_framework import generics
from emp_app.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAdminUser, AllowAny,DjangoModelPermissionsOrAnonReadOnly, BasePermission, SAFE_METHODS


class PostUserWritePermission(BasePermission):
    message = "Editing employee data is restricted to the author only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user



class EmployeeList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView,BasePermission):
    permission_classes = [AllowAny]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer