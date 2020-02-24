from django.db import models

# Create your models here.

class event(models.Model):
    title=models.CharField(max_length=200)
    event_date=models.DateField()
    Image=models.ImageField(upload_to='images/',default='Null')
    # venue=models.CharField(max_length=200)
    # manager=models.CharField(max_length=200)
    Desription=models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return (self.Desription[:50])
    
