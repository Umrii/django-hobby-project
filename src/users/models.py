from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField, USPostalCodeField
from .utils import user_directory_path
# Create your models here.





class Location(models.Model):
    address_1=models.CharField(max_length=128,blank=True)
    address_2=models.CharField(max_length=128,blank=True)
    city=models.CharField(max_length=64)
    state=USStateField(default='None')
    zip_code=USPostalCodeField(blank=True)

    def __str__(self):
          return f'Location {self.id}'
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path,null=True,blank=True)
    bio=models.CharField(max_length=140,blank=True)
    phone_number=models.CharField(max_length=12,blank=True)
    location=models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

