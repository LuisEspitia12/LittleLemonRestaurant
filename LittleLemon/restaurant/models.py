from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    BookingDate = models.DateField()
    No_of_guests = models.SmallIntegerField(default=2)

    def __str__(self): 
        return self.Name


# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10, decimal_places=2)   
   inventory = models.IntegerField(default=5)

   def __str__(self):
      return f'{self.title} : {str(self.price)}'