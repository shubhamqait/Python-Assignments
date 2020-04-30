from rest_framework import serializers
from employee.models import Employee
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='employee-highlight', format='html')

    class Meta:
        model = Employee
        fields = ['url','eid','highlight','ename','eemail','econtact','owner']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    employee = serializers.HyperlinkedRelatedField(many=True, view_name='employee-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url','eid', 'username', 'employee']