from django.db import models
import re



# Create your models here.
class accountManager(models.Manager):
    def acc_validator(self, postData):
        errors = { }
        if (len(postData['firstname']) < 2) or not re.match("^[A-Za-z]*$", postData['firstname']):
            errors["name"] = "First name must be greater than two characters and all letters."
        if (len(postData['lastname']) < 2) or not re.match("^[A-Za-z]*$", postData['lastname']):
            errors["name"] = "Last name must be greater than two characters and all letters."
        if (len(postData['email']) < 3) or not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
            errors["name"] = "Email must have at least 3 characters and have an @ sign with a period trailing somewhere after."
        if len(postData['password']) < 8:
            errors["name"] = "Password must be at least 8 characters long."
        if postData['password'] != postData['password2']:
            errors["name"] = "Password must match."
        return errors

class Account(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    objects = accountManager()