from django.db import models

class RegistrationForm(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    roll_no = models.IntegerField(unique = True, null=True)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    address = models.TextField()
    class Meta:
        db_table = "student"