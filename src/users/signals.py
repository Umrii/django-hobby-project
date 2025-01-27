from .models import Profile,Location
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=Profile)
def create_profile_location(sender,instance,created,**kwargs):
    if created:
        location = Location.objects.create()
        # Associate the Location with the Profile
        instance.location = location
        instance.save()




