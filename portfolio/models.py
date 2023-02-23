from django.db import models
'''Pillow must be installed'''


class Project(models.Model):
    '''Programmatic Name'''
    name = models.CharField(max_length=254, null=True, blank=True)
    type = models.CharField(max_length=254, null=True, blank=True)
    github = models.CharField(max_length=254, null=True, blank=True)
    website = models.CharField(max_length=254, null=True, blank=True)
    image_front = models.ImageField(null=True, blank=True)
    image_back = models.ImageField(null=True, blank=True)
    image_mockup = models.ImageField(null=True, blank=True)
    code = models.TextField(max_length=1000, null=True, blank=True)
    crud = models.TextField(max_length=1000, null=True, blank=True)
    api = models.TextField(max_length=1000, null=True, blank=True)
    description = models.TextField(max_length=1500, null=True, blank=True)
    letter = models.CharField(max_length=254, null=True, blank=True)
    position = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
