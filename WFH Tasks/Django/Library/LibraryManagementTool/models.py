from django.db import models

# Create your models here.
class Books(models.Model):
    isbn = models.IntegerField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    genere = models.CharField(max_length=30)
    quantity = models.IntegerField(max_length=6)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.author

    class Meta:
        db_table = "LibraryManagementTool"
