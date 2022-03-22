from django.db import models

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)




class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=11)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name