from django.db import models


class Person(models.Model):
    user_name=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)


    def __str__(self):
        return self.user_name

