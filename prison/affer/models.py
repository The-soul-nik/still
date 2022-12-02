from django.db import models

# Create your models here.from django.db import models

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    thumb = models.ImageField(default='default.png', blank=True, upload_to='media')

    def __str__(self):
        return self.title