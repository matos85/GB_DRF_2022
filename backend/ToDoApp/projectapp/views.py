from rest_framework.viewsets import ModelViewSet
from .models import ProjectModel, ToDoModel
from .serializers import ProjectModelSerializer
from .serializers import ToDoModelSerializer

from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilter


# from todo.models import Project, Todo
# from todo.serializers import ProjectModelSerializer, TodoModelSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter

    def get_queryset(self):
        queryset = ProjectModel.objects.all()
        name = self.request.query_params.get('name_project')
        if name is not None:
            queryset = queryset.filter(name__contains=name_project)
        return queryset


class TodoModelViewSet(ModelViewSet):
    class TodoLimitOffsetPagination(LimitOffsetPagination):
        default_limit = 20

    queryset = ToDoModel.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_class = ProjectFilter

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()




# class ProjectLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ProjectModelSerializer
#     pagination_class = ProjectLimitOffsetPagination
#
#
# class ToDoLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
#     queryset = ToDoModel.objects.all()
#     serializer_class = ToDoModelSerializer
#     pagination_class = ToDoLimitOffsetPagination

#
# class ProjectAppModelViewSet(ModelViewSet):
#     queryset = ProjectModel.objects.all()
#     serializer_class = ProjectModelSerializer
#
#
# class ToDoModelViewSet(ModelViewSet):
#     queryset = ToDoModel.objects.all()
#     serializer_class = ToDoModelSerializer
#
