from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= "CASCADE" )
    Name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    # cin = models.IntegerField()
    # registrationdate = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(default='default.png', blank=True)
    #author = models.ForeignKey(User, default=None)
    completed_form = models.BooleanField(default=False)


    def __str__(self):
        return self.Name

    def snippet(self):
        return self.body[:50] + '...'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, raw, **kwargs):
    if not raw:
        if created:
            Profile.objects.create(user=instance)
        else:
            instance.profile.save()
