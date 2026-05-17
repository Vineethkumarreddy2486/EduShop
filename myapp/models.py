from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    c_image=models.ImageField(upload_to='image/')
    c_name=models.CharField(max_length=250)
    c_desc=models.TextField()
    c_price=models.IntegerField()
    c_author=models.CharField(max_length=50)

class Account(User):
    phone=models.CharField(max_length=13)
    adress=models.CharField(max_length=100)

class Cart(models.Model):
    courses=models.ForeignKey(Course,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=0)












