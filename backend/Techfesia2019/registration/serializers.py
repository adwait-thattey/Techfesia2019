from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'college_name', 'profile_picture')
        read_only_fields = ('date_joined', 'last_login',)
        write_only_fields = ('password',)


