from django.db import models
from account.models import User

# Create your models here.
class UserFile(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    slug = models.SlugField(unique=True,blank=True,null=True)
    owner =  models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    file = models.FileField(upload_to="uploads/files")
    def __str__(self):
        return self.title
