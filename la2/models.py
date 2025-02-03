from django.db import models

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

