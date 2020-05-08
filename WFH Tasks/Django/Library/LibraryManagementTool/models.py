from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Books(models.Model):
    isbn = models.IntegerField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey("LibraryManagementTool.Author", on_delete=models.CASCADE)
    genere = models.CharField(max_length=30)
    quantity = models.IntegerField(max_length=6, default=0)
    available = models.BooleanField()


    def __str__(self):
        return self.title

    class Meta:
        db_table = "LibraryManagementTool"

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

@receiver(post_save, sender=Books)
def my_callback(sender, created, **kwargs):
    if not created:
        sender.available = False
    else:
        sender.available = True