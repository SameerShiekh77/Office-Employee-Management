from rest_framework import serializers
from emp_app.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'depart', 'salary', 'bonus','phone','role')