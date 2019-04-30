from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AccountDetail(models.Model):
    Name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    cin = models.IntegerField()
    # registrationdate = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(default='default.png', blank=True)
    #author = models.ForeignKey(User, default=None)

    def __str__(self):
        return self.Name

    def snippet(self):
        return self.body[:50] + '...'
