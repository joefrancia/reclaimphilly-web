from django.http import HttpResponse, Http404
import json
from services import LocationService
import validations
import conversions
import unicodedata
from reclaimphilly_web.models import Location

location_service = LocationService()

def get_locations_in_radius(request, latitude, longitude, radius=0):
    """
    Gets a list of locations_dict within a given mile radius.
    
	Returned, is a JSON-encoded list of dictionaries. Each dictionary
	may have the following keys:
	- id
	- latitude
	- longitude
	- address
	- picture (URL)
	- description
	- type   TODO This is coming back as the DB string, not the descriptive English version -- change that
	
	Example Request:
	http://localhost:8000/services/locations_dict/latitude/37.95/longitude/-70.00/radius/5
    """
    
    # Perform search
    locations_dict = location_service.get_locations(float(latitude), float(longitude), float(radius))
    locations_list = conversions.locations_to_detailed_coordinate_list(locations_dict)
    
    json_result = "[]"
    if locations_dict:
        json_result = json.dumps(locations_list) 
    
    return HttpResponse(json_result, mimetype="application/json", content_type="application/json; charset=utf8") # switch content_type to 'application/javascript for easier debug in browser

def get_location_by_id(request, id):
	"""
	Gets a single Location by its database ID column

	Returned, is a JSON-encoded location object with the following properties 
	- id
	- latitude
	- longitude
	- address
	- picture (URL)
	- description
	- type   TODO This is coming back as the DB string, not the descriptive English version -- change that	
	"""
	location = Location.objects.get(id=id)
	
	location_dict = conversions.location_to_detailed_coordinate_dict(location)
	
	json_result = "[]"
	if location:
		json_result = json.dumps(location_dict)
	
	return HttpResponse(json_result, mimetype="application/json", content_type="application/json; charset=utf8") # switch content_type to 'application/javascript for easier debug in browser
	

#def add_location(request):
#	latitude = None
#	longitude = None
#	
#	# Get all the parameters
#	params = request.GET
#	try:
#		latitude = float(params["latitude"])
#		longitude = float(params["longitude"])
#		# TODO add other types in here
#	except:
#		raise Http404 #TODO This error should be something else and have an error message attached
#
#	# Validate parameters
#	if not validations.is_number(latitude) or not validations.is_number(longitude):
#	   raise Http404 #TODO This error should be something else and have an error message attached
#
#	location_service.add_location(latitude, longitude)
#	
#	json_result = "[]"
#	
#	return HttpResponse(json_result, mimetype="application/json", content_type="application/json; charset=utf8") # switch content_type to 'application/javascript for easier debug in browser
