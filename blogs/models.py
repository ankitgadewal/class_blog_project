from django.db import models
from datetime import datetime
# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    datetime = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title

class Users(models.Model):
    comment = models.ForeignKey(Blogs, on_delete=models.CASCADE)

