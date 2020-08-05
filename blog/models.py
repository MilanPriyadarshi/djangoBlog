from django.db import models

# Create your models here.
class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    desc=models.TextField()
    author=models.CharField(max_length=100)
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return 'Post from '+self.author 
