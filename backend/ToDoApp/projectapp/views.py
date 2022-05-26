from rest_framework.viewsets import ModelViewSet
from .models import ProjectModel
from .serializers import ProjectModelSerializer


class ProjectAppModelViewSet(ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelSerializer