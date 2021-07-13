from django.db import models
from django.contrib.auth.models import User

        

class Flower(models.Model):
    name = models.CharField(max_length=80)
    water_time = models.IntegerField()
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1, db_column="owner_id")
    
    
    def __str__(self):
        return self.name