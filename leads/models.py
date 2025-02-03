from django.db import models
from django.db.models.signals import post_save
# from django.contrib.auth import get_user_model # using default django user
from django.contrib.auth.models import AbstractUser # using custom django user

# Create your models here.
# using custom django user
class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

# class Agent(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# User = get_user_model() # using default django user

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # to access user profile as user.profile
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True) # to access user profile as user.profile

    def __str__(self):
        return self.user.username

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
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username #.email
    


def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User) # this will create a user profile for every user created