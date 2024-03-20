from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self)-> str:
        return self.title
    
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField(max_length=200)
    description=models.TextField()
    image=models.CharField(max_length=400)

# class User(models.Model):
#     def __str__(self) -> str:
#         return self.username
    
#     username = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     password=models.CharField(max_length=200)
