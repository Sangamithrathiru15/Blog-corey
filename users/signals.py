#this signals are used to create a profile for every user when they are signing up with the username, default image and email id...nstead of creating it through admin page




from django.db.models.signals import post_save#this gets triggered when an object gets saved. when a user is created
from django.contrib.auth.models import User#sendr will send the signal
from django.dispatch import receiver#will receive the signal and perform task
from .models import Profile

#to create a user profile when the user is created

@receiver(post_save,sender=User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):#**kwargs can accept any number of arguments
    instance.profile.save()