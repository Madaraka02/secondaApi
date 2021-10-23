from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class comapny(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     reg_no = models.CharField(max_length=255)
#     slug = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ('-id')
#         verbose_name = "Companies"    

class Jobs(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    required_skills = models.TextField()
    status_open = models.BooleanField(default=True)
    comapny = models.ForeignKey(User, on_delete=models.CASCADE)
    apply = models.BooleanField(default=False)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ('-id',)    

