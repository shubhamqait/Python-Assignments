from django.db import models


class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)
    owner = models.ForeignKey('auth.User', related_name='employee', on_delete=models.CASCADE)
    highlighted = models.TextField()  
    class Meta:  
        db_table = "employee"  
