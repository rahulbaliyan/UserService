from rest_framework import serializers
from UserDetailsApp.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'company_name', 'city', 'age', 'state', 'zip', 'email')