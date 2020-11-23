from django.db import models

class Post(models.Model):

    STATUS = (
        ('doing', 'DOING'),
        ('done', 'DONE')
    )

    title = models.CharField(max_length=256)
    description = models.TextField()

    done = models.CharField(

        max_length=5, 
        choices= STATUS,
    )

    createad_at = models.DateField(auto_now_add=True)
    updatead_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.
