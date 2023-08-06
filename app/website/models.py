from django.db import models

# Create your models here.
class Food(models.Model):
    TYPES = [
            ("HQP", "High-quality protein source"),
            ("HQPF", "High-quality protein with fats"),
            ("CC", "Complex carbohydrates"),
            ("F", "Fiber"),
    ]
    name = models.CharField(max_length=60)
    kind = models.CharField(max_length=4, choices=TYPES)
    
    def __str__(self):
        return self.name
