
# Child of the AbstractBaseUser class 
from django.contrib.auth.models import AbstractUser 
from django.db import models

# Create your models here.
# Verifiy if there's positive integer. Takes 'null' or no input
# Null: Databse-related. Meaning No value. Python uses 'None' class. 
# Blank: Validation-related. Allows an empty value in a form
# Together these can store and empty 'no value' in the DB. 
class CustomUser(AbstractUser):
        age = models.PositiveIntegerField(null = True, blank=True)
        nice_name = models.CharField(null = True, blank=True, max_length=50)