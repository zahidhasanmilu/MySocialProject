from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='App_Login/Profile_Pic/', blank=True , null=True)
    dob = models.DateField(blank=True , null=True)
    website = models.URLField(blank=True , null=True)
    facebook = models.URLField(blank=True , null=True)


    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'