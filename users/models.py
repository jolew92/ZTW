from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
   # picture = models.ImageField(update_to='profile_image', blank=True)

    def __unicode__(self):
        return self.user.username