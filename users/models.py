from django.db import models

class User(models.Model):
    username = models.CharField("Username", max_length=64)
    first_name = models.CharField("First_name", max_length=64)
    last_name = models.CharField("Last_name", max_length=64)
    email = models.CharField("Email", max_length=64, unique=True)