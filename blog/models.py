from django.db import models

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    desc=models.TextField()
    author=models.CharField(max_length=100)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    image=models.ImageField(upload_to="blog/images",default="")

    def __str__(self):
        return self.title +'Post from '+self.author 
