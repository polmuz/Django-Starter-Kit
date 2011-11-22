from django.db import models

# Create your models here.

class MyModel(models.Model):
    """ My nice model """
    myfield = models.TextField()

    def get_upper_myfield(self):
        """ Get myfield in uppercase """
        return self.myfield.upper()
