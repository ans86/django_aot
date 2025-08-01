from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='default.jpg')
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"Game: {self.name}"