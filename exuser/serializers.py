from rest_framework import serializers
from exuser.models import Nuser

class NuserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Nuser
        fields='__all__'
