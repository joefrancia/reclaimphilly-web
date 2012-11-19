from django.db import models

# Create your models here.
class Location (models.Model):
	"""
	Represents a geographic location with the following properties:
	- latitude (required): Between -90 and 90
	- longitude (required): Between -180 and 180
	- type (required): Either "bldg" or "lot" 
	- address (optional): Stret address
	- description (optional): Description of the Location 
	- picture (optional): An image of the Location
	"""

	# Physical location data
	latitude = models.DecimalField(max_digits=15, decimal_places=13)
	longitude = models.DecimalField(max_digits=15, decimal_places=13)
	address = models.CharField(max_length=200, blank=True, null=True)
	
	# Other info
	LOCATION_TYPES = (
		("bldg", "Building"),
		("lot", "Lot"),
	)
	type = models.CharField(max_length="4", choices=LOCATION_TYPES)
	
	description = models.CharField(max_length="200", blank=True, null=True)
	picture = models.ImageField(upload_to="images/locations", blank=True, null=True)
	
	def __unicode__(self):
		return "(" + str(self.id) + ") Latitude: " + str(self.latitude) + ", " + "Longitude: " + str(self.longitude);