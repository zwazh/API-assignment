# API-assignment

import urllib2, json

# Replace this with your own
API_KEY = '6762c5fba6cf496e91d527f06213e05f'

########## YOUR CODE GOES HERE ##########

def get_bills(state, subjects):
    '''
    This function should accomplish the following tasks:
      - Open a connection to the /bills/ endpoing of Sunlight Foundation's OpenStates API:
        http://sunlightlabs.github.io/openstates-api/bills.html#methods/bill-search
      - Retrieve an API response with bills from the current legislative session in Missouri
      - print the titles of bills that contain "Transportation" in the "subjects" list
    '''
    response = urllib2.urlopen('http://openstates.org/api/v1/bills/?state=%s&search_window=session&subject=%s&apikey=%s' % (state, subjects, API_KEY))
    json_object = json.load(response)

    for bills in json_object:
      print bills['title'] 

    return

########## RUN FUNCTIONS HERE ##########

# Uncomment this to run your function with the appropriate arguments, as specified above
get_bills('mo', 'Transportation')
