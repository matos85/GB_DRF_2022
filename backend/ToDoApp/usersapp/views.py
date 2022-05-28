from rest_framework.viewsets import ModelViewSet
from .models import UsersappModel
from .serializers import UsersAppModelSerializer
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet


class UsersAppModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                             viewsets.GenericViewSet):
    queryset = UsersappModel.objects.all()
    serializer_class = UsersAppModelSerializer
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]



