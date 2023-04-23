from django.db import models

# Create your models here.

class Project(models.Model):
    #A project.
    name = models.CharField\
           (max_length=50, \
            help_text="The name of the Project.")
def __str__(self):
	return self.name

class Task(models.Model):
    #The tasks of a project.
    name = models.CharField\
            (max_length=70, \
             help_text="The name of the task.")
    project = models.ForeignKey\
                (Project, on_delete=models.CASCADE)
def __str__(self):
	return self.name
