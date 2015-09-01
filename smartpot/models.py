from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Plant(models.Model):
	scientific_name = models.CharField(max_length=200)
	plant_type = models.CharField(max_length=200)

        class Meta:
		verbose_name = "Plant"
		verbose_name_plural = "Plants"
	

class Pot(models.Model):
	secret_token = models.CharField(max_length=200)
	hardware_id = models.CharField(max_length=200)
	plant = models.ForeignKey(Plant)
	is_active = models.BooleanField(default=False)
	is_connected = models.BooleanField(default=False)
	


class PotUsers(models.Model):
	pot = models.ForeignKey(Pot)
	username = models.ForeignKey(User)

	class Meta:
		verbose_name = "Pot User"
		verbose_name_plural = "Pot Users"

class SensorData( models.Model) :
	pot = models.ForeignKey(Pot)
	sunlight = models.FloatField()
	moisture = models.FloatField()
	current_time = models.TimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Sensor Data"

# There could be others forms of data as well
class PotData(models.Model):
	pot = models.ForeignKey(Pot)
	sensor_data = models.ForeignKey(SensorData)

	class Meta:
		verbose_name_plural = "Pot Data"

