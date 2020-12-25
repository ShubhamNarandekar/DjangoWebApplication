from django.db import models

# Create your models here.
class member(models.Model):
    username = models.EmailField()
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.username + "\t" + self.password


