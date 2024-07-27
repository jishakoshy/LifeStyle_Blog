from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField( max_length=200)
    content = models.TextField()
    created_by = models.DateTimeField()
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    # categories = models.ManyToManyField("Category", related_name= "posts")

class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete= models.CASCADE)
    content = models.TextField()
    Comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)

