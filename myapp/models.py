from django.db import models

class PersonPerson(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):  
        return self.name



