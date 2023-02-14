from django.db import models

class Project(models.Model):
    project_name = models.CharField("Projectname", max_length=64)
    repo_link = models.URLField("Repolink")
    authors = models.CharField("Authors", max_length=128)

class TODO(models.Model):
    projeck = models.ManyToManyField(Project)
    text = models.TextField()
    creation_date = models.DateTimeField("Creationdate")
    update_date = models.DateTimeField("Updatedate", auto_now=True)
    user = models.CharField("User", max_length=64)
    choice_status = (("active",'активно',),('close','закрыто'))
    status = models.CharField(max_length=300, choices = choice_status)