from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.title

