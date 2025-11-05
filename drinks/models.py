from django.db import models

# Create your models here.

class Drink(models.Model):
    CATEGORY_CHOICES = [
        ('tea', 'Tea'),
        ('coffee', 'Coffee'),
        ('cocktail', 'Cocktail'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    moods = models.JSONField(default=list)
    weather = models.JSONField(default=list)
    time_of_day = models.JSONField(default=list)
    season = models.JSONField(default=list)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name