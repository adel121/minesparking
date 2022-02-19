from django.db import models
import datetime
import django.utils

# Create your models here.



class Car(models.Model):
	Registry = models.CharField(max_length = 100)

	def __str__(self):
		return self.Registry


class Driver(models.Model):
	Name = models.CharField(max_length=100)
	Surname = models.CharField(max_length=100)
	Email = models.EmailField(max_length=254)
	Telephone = models.CharField(max_length=30)

	def __str__(self):
		return self.Name + " " + self.Surname


class Door(models.Model):
	State = models.CharField(max_length=100, choices=[('closed','closed'),('open','open')],default='closed')

	def __str__(self):
		return self.State + " Door"




class Position(models.Model):
	Type = models.CharField(max_length = 100, choices=[('normal','normal'),('anomalous','anomalous')],)
	Rank = models.IntegerField()

	def __str__(self):
		return self.Type + " " + str(self.Rank)


class Occupies(models.Model):
	Car = models.ForeignKey(Car,on_delete=models.CASCADE)
	Position = models.ForeignKey(Position,on_delete=models.CASCADE)

	def __str__(self):
		return self.Car.Registry + ' - ' + str(self.Position.Rank)

class Drives_Car(models.Model):
	Driver = models.ForeignKey(Driver,on_delete = models.CASCADE)
	Car = models.ForeignKey(Car,on_delete=models.CASCADE)
	Pub_Time =  models.DateTimeField(default =django.utils.timezone.now())
	def __str__(self):
		return self.Driver.Name + " " + self.Driver.Surname + "-" + self.Car.Registry


class Pending_Request(models.Model):
	Registry = models.CharField(max_length = 100)
	Verification_Code = models.CharField(max_length = 100, default="unverified")
	Last_Captured = models.DateTimeField(default =django.utils.timezone.now())
	Status = models.CharField(max_length=100, choices = [ ('pending','pending'), ('in progress','in progress'), ('verified', 'verified')], default = 'pending')
	Driver = models.ForeignKey(Driver,on_delete = models.CASCADE, null = True)
	def __str__(self):
		return self.Registry


class Capture(models.Model):
    State = models.CharField(max_length=100, choices=[('allowed','allowed'),('not allowed','not allowed')],default='not allowed')
    LastAllowed = models.DateTimeField(default =django.utils.timezone.now())

    def __str__(self):
        return self.State + " - Last allowed at: " + str(self.LastAllowed)










