from django.db import models
import re, bcrypt

# Create your models here.
class accountManager(models.Manager):
    def acc_validator(self, postData):
        errors = { }
        if len(postData['firstname']) < 2 or not re.match("^[A-Za-z]*$", postData['firstname']):
            errors["firstname"] = "First name must be greater than two characters and all letters."
        if len(postData['lastname']) < 2 or not re.match("^[A-Za-z]*$", postData['lastname']):
            errors["lastname"] = "Last name must be greater than two characters and all letters."
        if len(postData['email']) < 3 or not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
            errors["email"] = "Email must have at least 3 characters and have an @ sign with a period trailing somewhere after."
        if account.objects.filter(email = postData['email']).exists():
            errors["emailtaken"] = "Email already exists!"
        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 characters long."
        if postData['password'] != postData['password2']:
            errors["password2"] = "Password must match."
        return errors
    def login_validator(self, postData):
        errors = { }
        if account.objects.filter(email = postData['loginemail']).exists():
            if not bcrypt.checkpw(postData['loginpassword'].encode(), account.objects.get(email=postData['loginemail']).password.encode()):
                errors["password3"] = "Password is wrong!"
        else:
            errors["emailnotexist"] = "Email doesn't exist!"
        return errors
    def update_validator(self, postData, sessionData):
        errors = { }
        if not account.objects.get(id=sessionData['id']).email == postData['email']:
            if account.objects.filter(email = postData['email']).exists():
                errors["emailexists"] = "Email already exists!"
        if len(postData['firstname']) < 2 or not re.match("^[A-Za-z]*$", postData['firstname']):
            errors["firstname"] = "First name must be greater than two characters and all letters."
        if len(postData['lastname']) < 2 or not re.match("^[A-Za-z]*$", postData['lastname']):
            errors["lastname"] = "Last name must be greater than two characters and all letters."
        if len(postData['email']) < 3 or not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
            errors["email"] = "Email must have at least 3 characters and have an @ sign with a period trailing somewhere after."
        return errors
            
        
class quoteManager(models.Manager):
    def quote_validator(self, postData):
        errors = { }
        if len(postData['author']) < 1:
            errors["authorlen"] = "Author field is empty!"
        if len(postData['quote']) < 1:
            errors["quotelen"] = "Quote length is empty!"
        return errors

class account(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    objects = accountManager()

class quote(models.Model):
    author = models.CharField(max_length=35)
    quote = models.CharField(max_length=200)
    email = models.ForeignKey(account, related_name="quotes")
    objects = quoteManager()