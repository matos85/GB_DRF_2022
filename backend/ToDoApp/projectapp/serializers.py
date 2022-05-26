from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ProjectModel


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'
