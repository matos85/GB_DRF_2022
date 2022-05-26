from rest_framework.viewsets import ModelViewSet
from .models import UsersappModel
from .serializers import UsersAppModelSerializer


class UsersAppModelViewSet(ModelViewSet):
    queryset = UsersappModel.objects.all()
    serializer_class = UsersAppModelSerializer
