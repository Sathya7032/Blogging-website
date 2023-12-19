from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=40)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_title = models.CharField(max_length=1000)
    category_image = models.ImageField(upload_to='photos')
    category_description = RichTextField() 
    category_date = models.DateTimeField() 
    url = models.CharField(unique=True,max_length=100)
    

    def __str__(self):
        return self.category_title
    
class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=1000)
    blog_image = models.ImageField(upload_to='photos')
    blog_description = RichTextField()
    blog_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.CharField(unique=True,max_length=100)

    def __str__(self):
        return self.blog_title

class Tutorial(models.Model):
    tutorial_id = models.AutoField(primary_key=True)
    tutorial_name = models.CharField(max_length= 100)
    url = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.tutorial_name       

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=100)
    post_file = models.FileField(upload_to='photos')
    post_description = RichTextField()
    post_date = models.DateTimeField()
    tutorial = models.ForeignKey(Tutorial,on_delete= models.CASCADE)
    url = models.CharField(unique=True,max_length=100)

    def __str__(self):
        return self.post_title    

