from django.db import models

# Create your models here.
class NotesModel(models.Model):
    title = models.CharField('Title', max_length=250)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return self.title