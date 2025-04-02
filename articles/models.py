from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.pk)])

class Comment(models.Model): #following relationships “backward”
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE,
        #We want to display all comments related to a specific article `QUERY`
        related_name='comments', # plural of our Comment` model`
        )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
        )

    def __str__(self):
       return self.comment

    def get_absolute_url(self): #get_absolute_url redirect URL to specific location#
        return reverse('article_list')
    #When str and getabsurl updated you have to make a new migration file
    #Keep migrations as small and contained as possible
