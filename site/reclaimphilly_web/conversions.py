"""
An assortment of functions that convert  models from one
type to another. Mostly used to prepare data for conversion
to JSON in web services.
"""


def location_to_coordinate_dict(location):
    """
    Converts a models.Location object
    to a dictionary containing two keys:
    - id
    - latitude
    - longitude
    """
    return { "latitude" : float(location.latitude),
           "longitude" : float(location.longitude),
           "id" : location.id}

    
def location_to_detailed_coordinate_dict(location):
	"""
	Converts a models.Location object
	to a dictionary containing the following keys:
	- id
	- latitude
	- longitude
	- address
	- picture
	- type
	- description
	
	If a property is None, it is populated with an empty
	string ('') 
	"""
	coord_dict = location_to_coordinate_dict(location)
	coord_dict["address"] = location.address or ''
	coord_dict["picture"] = location.picture or ''
	coord_dict["type"] = location.type or ''
	coord_dict["description"] = location.description or ''

	return coord_dict

def locations_to_coordinate_list(locations):
	"""
	Converts a list of models.Location objects
	to a list of dictionaries containing two keys:
	- id
	- latitude
	- longitude
	"""
	coord_list = []
	for location in locations:
		coordDict = location_to_coordinate_dict(location)
		coord_list.append(coordDict)
        
	return coord_list

def locations_to_detailed_coordinate_list(locations):
	"""
	Converts a list of models.Location objects
	to a list of dictionaries containing the following keys:
	- latitude
	- longitude
	- address
	- picture
	- type
	- description
	
	If a property is None, it is populated with an empty
	string ('') 
	"""
	coord_list = []
	for location in locations:
		coordDict = location_to_detailed_coordinate_dict(location)
		coord_list.append(coordDict)
        
	return coord_list
