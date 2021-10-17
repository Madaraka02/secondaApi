from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jobs(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    required_skills = models.TextField()
    status_open = models.BooleanField(default=True)
    comapny = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ('-id',)    
