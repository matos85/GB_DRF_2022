from rest_framework.viewsets import ModelViewSet
from .models import ProjectModel, ToDoModel
from .serializers import ProjectModelSerializer
from .serializers import ToDoModelSerializer


class ProjectAppModelViewSet(ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelSerializer



class ToDoModelViewSet(ModelViewSet):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoModelSerializer