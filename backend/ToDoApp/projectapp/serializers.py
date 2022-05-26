from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ProjectModel, ToDoModel


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'




class ToDoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDoModel
        fields = '__all__'

