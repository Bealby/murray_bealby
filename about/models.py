from django.db import models
'''Pillow must be installed'''


class About(models.Model):
    '''Programmatic Name'''
    name = models.CharField(max_length=254, null=True, blank=True)
    description_1 = models.TextField(max_length=1000, null=True, blank=True)
    description_2 = models.TextField(max_length=1000, null=True, blank=True)
    hobby_1 = models.TextField(max_length=1000, null=True, blank=True)
    hobby_2 = models.TextField(max_length=1000, null=True, blank=True)
    hobby_3 = models.TextField(max_length=1000, null=True, blank=True)
    hobby_4 = models.TextField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return self.name