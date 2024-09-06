from django.db import models
# from django.contrib.auth import get_user_model # using default django user
from django.contrib.auth.models import AbstractUser # using custom django user

# Create your models here.
# using custom django user
class User(AbstractUser):
    pass

# class Agent(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# User = get_user_model() # using default django user

class Lead(models.Model):
    # SOURCE_CHOICES = (
    #     ('Youtube', 'Youtube'),
    #     ('Twitter', 'Twitter'),
    #     ('Facebook', 'Facebook'),
    # )
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)

    # phoned = models.BooleanField(default=False)   
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)

    # agent = models.ForeignKey('Agent', on_delete=models.SET_DEFAULT, null=True, default=1) #assuming category 1 is default eg 'no_agent_assigned', or some agent selected randomly or criteria based 

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username #.email