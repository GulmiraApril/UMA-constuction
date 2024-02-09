from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    message = models.TextField(null=True, blank=True)
    is_solved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'name: {self.name}'


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'name: {self.name}'






