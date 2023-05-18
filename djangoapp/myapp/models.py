from django.db import models  
  
class RoomAllocation(models.Model):  
    Name= models.CharField(max_length=30)  
    Student_Id = models.CharField(max_length=20) 
    Block = models.CharField(max_length=30) 
    Room_number = models.CharField(max_length=30) 
    class Meta:  
        db_table = "RoomAllocation"

from django.db import models  

class RoomDetails(models.Model):  
    Name_of_block = models.CharField(max_length=30)  
    Room_number = models.CharField(max_length=10) 
    Furnitures_present = models.CharField(max_length=500) 
    About_toilet = models.CharField(max_length=500)
    class Meta:  
        db_table = "RoomDetails"

from django.db import models

class login(models.Model):
    user_id = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = "login"

from django.db import models

class maintenance(models.Model):
    Name = models.CharField(max_length=30)
    Year = models.CharField(max_length=50)
    Name_of_block = models.CharField(max_length=30)
    Room_number = models.CharField(max_length=50)
    Maintenance_needed = models.CharField(max_length=100)
    class Meta:
        db_table = "maintenance"
    
from django.db import models

class Guideline(models.Model):
    Rules = models.CharField(max_length=100) 
    Mess_rules = models.CharField(max_length=100) 
    class Meta:  
        db_table = "Guideline"


from django.db import models

class Notification(models.Model):
    noti = models.CharField(max_length=1000) 
    class Meta:  
        db_table = "Notification"