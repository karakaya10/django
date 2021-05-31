from django.db import models

from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=250, default="")
    content = RichTextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/',null=True)
    keywords = models.TextField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class About(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name