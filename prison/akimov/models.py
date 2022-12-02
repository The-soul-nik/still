from django.db import models


class New(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	thumb = models.ImageField(default='default.png', blank=True)

def __str__(self):
	return self.name