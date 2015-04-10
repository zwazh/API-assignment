# API-assignment

import urllib2, json

# Replace this with your own
API_KEY = '6762c5fba6cf496e91d527f06213e05f'

def sample_function(name):
    print 'I am a sample function'
    print 'My name is %s' % name
    return

########## YOUR CODE GOES HERE ##########

def get_bills(state, type):
    response = urllib2.urlopen('http://openstates.org/api/v1/bills/?state=mo&apikey=6762c5fba6cf496e91d527f06213e05f')
    json_object = json.load(response)

    for bills in json_object:
      if bills['state'] == 'mo':
        print bills

        if bills['subjects'] == 'Transportation':
          print bills['title']

    '''
    This function should accomplish the following tasks:
      - Open a connection to the /bills/ endpoing of Sunlight Foundation's OpenStates API:
        http://sunlightlabs.github.io/openstates-api/bills.html#methods/bill-search
      - Retrieve an API response with bills from the current legislative session in Missouri
      - print the titles of bills that contain "Transportation" in the "subjects" list
    '''
    return

########## RUN FUNCTIONS HERE ##########

sample_function('Chase')

# Uncomment this to run your function with the appropriate arguments, as specified above
get_bills('mo', 'Transportation')
