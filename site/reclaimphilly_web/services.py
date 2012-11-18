from models import Location
from django.contrib.auth.models import User

class LocationService():
	"""
	Performs convenience search and data access functions for Location objects
	"""

	MILE_PER_DEGREE_LATITUDE = (1.0 / 69.0)
	MILE_PER_DEGREE_LONGITUDE = (1.0 / 49.0) # Approximate, since this changes depending on how far North or South, 49 is at 45 degress (or halfway between equator and poles)

	def get_locations(self, latitude, longitude, mile_radius):
		"""
		Retrieves a list of all Location objects within a specified mile radius
		from a given point (latitude and longitude).

		If none are found, returns an empty list.
		"""
		latitude_diff = mile_radius * LocationService.MILE_PER_DEGREE_LATITUDE
		upper_bound_latitude = latitude + latitude_diff
		lower_bound_latitude = latitude - latitude_diff

		longitude_diff = mile_radius * LocationService.MILE_PER_DEGREE_LONGITUDE
		upper_bound_longitude = longitude + longitude_diff
		lower_bound_longitude = longitude - longitude_diff

		locations = Location.objects.filter(latitude__lte=upper_bound_latitude,
										latitude__gte=lower_bound_latitude,
										longitude__lte=upper_bound_longitude,
										longitude__gte=lower_bound_longitude)

		return locations

	def add_location(self, latitude, longitude, type, address=None, picture=None, description=None):
		"""
		Adds a new Location object to the database
		
		Returns the newly created Location object
		"""
		new_location = Location()
		new_location.latitude = latitude
		new_location.longitude = longitude
		new_location.address = address
		new_location.type = type
		new_location.picture = picture
		new_location.description = description
		new_location.save()
		
		return new_location


	def get_location(self, latitude, longitude):
		"""
		Gets a Location object from a given point (latitude and longitude).

		If a matching Location object isn't found, returns None
		"""
		try:
			return Location.objects.get(latitude=latitude, longitude=longitude)
		except: # Entry.DoesNotExist:
			return None