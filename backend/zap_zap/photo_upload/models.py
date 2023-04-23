from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

# from video
def get_upload_path(instance, filename):
    # in the str, it used to be .pk but I figured target name would be better, but if it doesn't work, then change back to pk
    return os.path.join('target_pics', filename)

# Create your models here.
class Target(models.Model):
    target_name = models.TextField()
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    # from video
    # image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)

    message_to_owner = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.target_name
    # TODO: FINISH IMPLEMENTING THIS AFTER FIGURING OUT PHOTOS
