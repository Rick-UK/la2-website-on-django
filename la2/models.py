from django.db import models
from django.urls import reverse


# Create your models here.
class News(models.Model):
    slug = models.SlugField(max_length=20, unique=True, verbose_name="Slug")
    is_published = models.BooleanField(default=False, verbose_name="Published")
    title = models.CharField(max_length=100, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('la2:news_detail_page', kwargs={'news_slug': self.slug})

class Servers(models.TextChoices):
    X2 = 'x2',
    X50 = 'x50',
    X1200 = 'x1200'

class Feedback(models.Model):
    userEmail = models.EmailField(max_length=256,verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    server = models.CharField(max_length=5, choices=Servers.choices, verbose_name="Server")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_at}: {self.userEmail}"

