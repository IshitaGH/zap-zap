from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Target(models.Model):
    target_name = models.TextField(User)
    image = models.ImageField(default='default_target.jpg', upload_to='target_pics')
    call_police = models.BooleanField(default=True)
    ring_alarm = models.BooleanField(default=True)
    message_contacts = models.BooleanField(default=True)
    message_to_contacts = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.target_name
    # TODO: FINISH IMPLEMENTING THIS AFTER FIGURING OUT PHOTOS
