from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

# Create your models here.



class Article(models.Model):

    user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title         = models.CharField(max_length=300)
    # content       = models.TextField()
    content       = RichTextField(blank=True, null=True)
    released_date = models.DateField('date published',auto_now_add=True)
    tags       = TaggableManager()
    likes   = models.ManyToManyField(User,related_name='blog_article')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.title}   |   {str(self.user)}'

    class Meta:
        ordering = ['-released_date']

    def get_absolute_url(self):
        return reverse('articles:article-detail', kwargs={'pk':self.pk})


class Profile(models.Model):

    _user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default-profile.jpg')

    def __str__(self):
        return f'{self._user.username} profile picture'



class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name    = models.CharField(max_length=80)
    email   = models.EmailField(null=True,blank=True)
    body    = models.TextField()
    created = models.DateField(auto_now_add=True)
    active  = models.BooleanField(default=True)
    

    def __str__(self):
        return f'{self.name}\'s comment on {self.article}'

    class Meta:
        ordering = ['-created']

