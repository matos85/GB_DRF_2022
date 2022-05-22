from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Usersapp


class UsersAppModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Usersapp
        fields = 'username, firstname, lastname, email'
        fields = '__all__'
