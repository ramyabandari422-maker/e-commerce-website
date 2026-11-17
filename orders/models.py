from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Orders(models.Model):
    options=[
        ("ordered","ordered"),("shipped","shipped"),("out of delivery","out of delivery0"),("delivered","deliverd")
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_price=models.IntegerField(default=0)
    status=models.CharField(max_length=66,choices=options,default="ordered")
    created_at=models.DateTimeField(auto_now_add=True)
    



    def __str__(self):
      return f"{self.status}"


