from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Jobs
 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
 
class  JobSerializer(serializers.HyperlinkedModelSerializer):
    company = UserSerializer(read_only=True)
    class Meta:
        model = Jobs()
        fields = '__all__'