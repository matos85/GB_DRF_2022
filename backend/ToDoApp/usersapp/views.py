from rest_framework.viewsets import ModelViewSet
from .models import Usersapp
from .serializers import UsersAppModelSerializer


class UsersAppModelViewSet(ModelViewSet):
    queryset = Usersapp.objects.all()
    serializer_class = UsersAppModelSerializer
