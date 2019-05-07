"""
__author__ = "Rahul kumar"
__version__ ="1.0"
__date__ = "May 7 15:48:15 2019"
__copyright__ = "©2019 rahul_kumar"

"""

from rest_framework import serializers
from UserDetailsApp.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'company_name', 'city', 'age', 'state', 'zip', 'email')