from django.db import models

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='')
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

