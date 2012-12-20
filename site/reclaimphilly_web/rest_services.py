from django.http import HttpResponse, Http404, HttpResponseBadRequest, \
	HttpRequest, HttpResponseServerError
import json
from services import LocationService
import validations
import conversions
import unicodedata
import re
from reclaimphilly_web.models import Location
from django.views.decorators.csrf import csrf_exempt

# Static / Class level objects
LOCATION_SERVICE = LocationService()
VALID_LOCATION_ID_REGEX = re.compile('^\d+$')
VALID_ADDRESS_REGEX = re.compile('^(\w|\.|\s|-)+$')
VALID_DESCRIPTION_REGEX = re.compile('^(\w|\.|\s|-|!|\?|\')+$')

@csrf_exempt
def get_locations_in_radius(request): # , latitude, longitude, radius=0
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
	http://localhost:8000/services/locations?latitude=1&longitude=2&radius=3
	GET Params
		- latitude - number
		- longitude - number
		- radius - number 
	"""
	# Validate request - must be GET
	if request.method != 'GET':
		return HttpResponseBadRequest('Request must be a GET request')
	
	# Validate latitude - required, number only
	try:
		latitude = request.GET['latitude']
		latitude = float(latitude)
	except:
		return HttpResponseBadRequest('Non-numeric or missing latitude parameter')
	
	# Validate longitude - required number only
	try:
		longitude = request.GET['longitude']
		longitude = float(longitude)
	except:
		return HttpResponseBadRequest('Non-numeric or missing longitude parameter')
	
	# Validate radius - required, number only
	try:
		radius = request.GET['radius']
		radius = float(radius)
	except:
		return HttpResponseBadRequest('Non-numeric or missing radius parameter')

	# Perform search
	locations_dict = LOCATION_SERVICE.get_locations(latitude, longitude, radius)
	locations_list = conversions.locations_to_detailed_coordinate_list(locations_dict)
	
	json_result = '[]'
	if locations_dict:
	    json_result = json.dumps(locations_list)
	
	return HttpResponse(json_result, mimetype='application/json', content_type='application/json; charset=utf8') # switch content_type to 'application/javascript for easier debug in browser

@csrf_exempt
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
	
	Sample request:
	http://localhost:8000/services/location/123
	
	ID is validated in urls config, no need to repeat here
	"""
	location = LOCATION_SERVICE.get_location(id=id)
	location_dict = conversions.location_to_detailed_coordinate_dict(location)
	
	json_result = "[]"
	if location:
		json_result = json.dumps(location_dict)
	
	return HttpResponse(json_result, mimetype='application/json', content_type='application/json; charset=utf8') # switch content_type to 'application/javascript for easier debug in browser
	
@csrf_exempt
def add_location(request): #, latitude, longitude, type, address=None, picture=None, description=None
	"""
	TODO document
	"""
	# Validate request - must be POST
	if request.method != 'POST':
		return HttpResponseBadRequest('Request must be a POST request')

	# Validate latitude - required, number only
	try:
		latitude = request.POST['latitude']
		latitude = float(latitude)
	except:
		return HttpResponseBadRequest('Non-numeric or missing latitude parameter')
	
	# Validate longitude - required, number only
	try:
		longitude = request.POST['longitude']
		longitude = float(longitude)
	except:
		return HttpResponseBadRequest('Non-numeric or missing longitude parameter')
		
	# Validate type - required, must be be a valid type
	try:
		type = request.POST['type']
		if not Location.VALID_TYPES.count(type):
			return HttpResponseBadRequest('Invalid type parameter. Valid options are: ' + str(Location.VALID_TYPES))
	except KeyError:
		return HttpResponseBadRequest('Missing type parameter. Valid options are ' + str(Location.VALID_TYPES))
	
	# Validate address - optional, must be only have letters, numbers, periods, and dashes
	try:
		address = request.POST['address']
		if address and not VALID_ADDRESS_REGEX.match(address):
			return HttpResponseBadRequest('Invalid address parameter. Can only contain letters, numbers, periods, and dashes')
	except KeyError:
		address = None
		
	# Validate picture - optional, must be under a certain size limit
	# TODO figure out how to do this
	try:
		picture = request.POST['picture']
	except KeyError:
		picture = None
	
	# Validate description - optional; limit to 200 characters; only letters, numbers, common punctuation, dashes
	try:
		description = request.POST['description']
		if description and len(description) > 200 and not VALID_DESCRIPTION_REGEX.match(description):
			return HttpResponseBadRequest('Invalid description parameter. Can only contain periods, question marks, exclamations, letters, numbers, and dashes')
	except KeyError:
		description = None
	
	# Add the location
	try:
		location = LOCATION_SERVICE.add_location(latitude, longitude, type, address, picture, description)
	except Exception as er:
		return HttpResponseServerError('Was unable to add the new location due to a server error')
	
	# return the location that was just added
	return get_location_by_id(request, location.id)