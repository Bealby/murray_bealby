from django.db import models
'''Pillow must be installed'''


class About(models.Model):
    '''Programmatic Name'''
    name = models.CharField(max_length=254, null=True, blank=True)
    description_1 = models.TextField(max_length=1000, null=True, blank=True)
    description_2 = models.TextField(max_length=1000, null=True, blank=True)
    hobbie_1 = models.TextField(max_length=1000, null=True, blank=True)
    hobbie_2 = models.TextField(max_length=1000, null=True, blank=True)
    hobbie_3 = models.TextField(max_length=1000, null=True, blank=True)
    hobbie_4 = models.TextField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return self.name