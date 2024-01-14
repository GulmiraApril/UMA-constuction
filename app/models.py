from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    message = models.TextField(null=True, blank=True)
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return f'name: {self.name}'


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    project_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'name: {self.project_name}'






