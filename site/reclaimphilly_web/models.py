from django.db import models

# Create your models here.
class Location (models.Model):

	# Physical location data
	latitude = models.DecimalField(max_digits=15, decimal_places=13)
	longitude = models.DecimalField(max_digits=15, decimal_places=13)
	address = models.CharField(max_length=200, blank=True)
	
	# Other info
	LOCATION_TYPES = (
		("bldg", "Building"),
		("lot", "Lot"),
	)
	type = models.CharField(max_length="4", choices=LOCATION_TYPES)
	
	description = models.CharField(max_length="200", blank=True)
	picture = models.ImageField(upload_to="images/locations", blank=True)
	
	def __unicode__(self):
		return "Latitude: " + str(self.latitude) + ", " + "Longitude: " + str(self.longitude);