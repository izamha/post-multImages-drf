import uuid
from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    image = models.FileField(upload_to='media')

    def __str__(self):
        return 'Image {}'.format(self.id)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    texts = models.TextField()
    images = models.ManyToManyField(Image, related_name='images', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = ('Posts')

    def __str__(self):
        return f"{self.id}"
