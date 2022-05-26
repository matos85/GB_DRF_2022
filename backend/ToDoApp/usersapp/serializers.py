from rest_framework.serializers import HyperlinkedModelSerializer
from .models import UsersappModel


class UsersAppModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UsersappModel
        fields = 'username, firstname, lastname, email'
        # fields = '__all__'
