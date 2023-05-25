from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.SlugField()
    descriptions = models.TextField()
    content = RichTextUploadingField()
    image = models.ImageField()
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = TaggableManager()

    def __str__(self) -> str:
        return self.title