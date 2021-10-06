import urllib.request
import json

def extract_data(list_of_dicts):                    #will extract important election data from json
    for dictionary in list_of_dicts:                           
        return f"Date: {dictionary['date'].split('T')[0]}, Election: {dictionary['description']}"

def return_api_results(city,state):
    url = f"https://api.turbovote.org/elections/upcoming?district-divisions=ocd-division/country:us/state:{state},ocd-division/country:us/state:{state}/place:{city}"
    r = urllib.request.Request(url)
    r.add_header("Accept", "application/json")
    with urllib.request.urlopen(r) as f:
        response_str = f.read().decode('utf-8')
        election_list = json.loads(response_str)    #list of dicts  
        election_info = extract_data(election_list) #extract helpful information for voters
        if election_list == []:                     #if api call returns no elections from entered city, state
            return('No upcoming elections')
        else:                                       #if api call does return election(s), print date and description
            return election_info



def test(city,state):
    return f"The address you entered is {city}, {state}"
