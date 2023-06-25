from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
