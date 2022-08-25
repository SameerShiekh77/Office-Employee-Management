from rest_framework import generics
from emp_app.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, BasePermission, SAFE_METHODS


class PostUserWritePermission(BasePermission):
    message = "Editing employee data is restricted to the author only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user



class EmployeeList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView,BasePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer