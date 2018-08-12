from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    posted_by = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    createdby = models.CharField(max_length=255)

    def __str__(self):
        return self.title