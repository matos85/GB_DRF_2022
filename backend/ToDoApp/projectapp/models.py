from django.db import models
from usersapp.models import UsersappModel

# Create your models here.
class ProjectModel(models.Model):
    name_project = models.CharField(max_length=64)
    link_project = models.CharField(max_length=1024)
    users_work = models.ManyToManyField(UsersappModel)


    def __str__(self):
        return self.name_project


class ToDoModel(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    text = models.TextField('Description', max_length=256)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UsersappModel, models.PROTECT)


    def __str__(self):
        return self.project
