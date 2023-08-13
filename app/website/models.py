from django.db import models
import random

# Create your models here.
class Food(models.Model):
    TYPES = [
            ("HQP", "High-quality protein "),
            ("HQPF", "High-quality protein with fats"),
            ("CC", "Complex carbohydrates"),
            ("SC", "Simple carbohydrates"),
            ("F", "Fiber"),
    ]
    name = models.CharField(max_length=60)
    kind = models.CharField(max_length=4, choices=TYPES)
    
    def __str__(self):
        return self.name

    def get_random_kind(food_type):
        items = list(Food.objects.filter(kind=food_type))
        random_item = random.choice(items)
        return random_item
    
    def generate_combo(combo):
        match combo:
            case "Breakfest":
                protein=Food.get_random_kind("HQP")
                carbohydrates=Food.get_random_kind("CC")
                fruit=Food.get_random_kind("SC")
                return str(protein) + '\n' + str(carbohydrates) + '\n' + str(fruit)
            case "Lunch":
                protein=Food.get_random_kind("HQPF")
                carbohydrates=Food.get_random_kind("CC")
                fiber=Food.get_random_kind("F")
                return str(protein) + '\n' + str(carbohydrates) + '\n' + str(fiber)
            case "Dinner":
                protein=Food.get_random_kind("HQP")
                carbohydrates=Food.get_random_kind("CC")
                fiber=Food.get_random_kind("F")
                return str(protein) + '\n' + str(carbohydrates) + '\n' + str(fiber)

            
        


