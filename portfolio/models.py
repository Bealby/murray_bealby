from django.db import models
'''Pillow must be installed'''


class Project(models.Model):
    '''Programmatic Name'''
    name = models.CharField(max_length=254)
    github = models.CharField(max_length=254)
    website = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    code = models.TextField(max_length=1000, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
