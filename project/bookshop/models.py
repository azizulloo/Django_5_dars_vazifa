from django.db import models

# Create your models here.


class Genre(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name




class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    description=models.TextField(null=True, blank=True)
    price=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    published=models.BooleanField(default=True)
    views=models.IntegerField(default=0)
    image=models.ImageField(upload_to="images/", null=True, blank=True)
    
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    