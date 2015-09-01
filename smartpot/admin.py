from django.contrib import admin

# Register your models here.
from smartpot.models import PotUsers,Pot,Plant,SensorData,PotData

admin.site.register(PotUsers)
admin.site.register(Pot)
admin.site.register(Plant)
admin.site.register(SensorData)
admin.site.register(PotData)

'''

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
                verbose_name = "PotUser"
                verbose_name_plural = "PotUsers"

class SensorData( models.Model) :
        pot = models.ForeignKey(Pot)
        sunlight = models.FloatField()
        moisture = models.FloatField()
        current_time = models.TimeField(auto_now_add=True)

        class Meta:
                verbose_name_plural = "SensorData"

# There could be others forms of data as well
class PotData(models.Model):
        pot = models.ForeignKey(Pot)
        sensor_data = models.ForeignKey(SensorData)

        class Meta:
                verbose_name_plural = "PotData"



'''
