from django.db import models

# Create your models here.
class About(models.Model):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length = 255)
    mydesc = models.TextField()
    pic =  models.ImageField(null = True)

    def __str__(self):
        return self.name