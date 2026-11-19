# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json

TotalEvents = 0
TotalFelt = 0
MostFeltEvent=""
MostFeltCount = 0
# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def quakes(data):
    if data['properties']['type'] is not None:
        return True
    return False


TotalEvents = len(list(filter(quakes, data['features'])))

TotalFelt = sum(True for q in data['features'] if q['properties']['felt'] is not None and q['properties']['felt']>=100)

mfs = max(data['features'], key=lambda x: x['properties']['felt'] if x['properties']['felt'] is not None else 0)
MostFeltEvent = 'M '+str(mfs['properties']['mag'])+' - ' + mfs['properties']['place']
MostFeltCount = mfs['properties']['felt']

tensig = sorted(data['features'],key=lambda x: x['properties']['sig'] if x['properties']['sig'] is not None else 0,reverse=True)[:10]
for t in tensig:
    print("{0} place with a significance of {1}".format(t['properties']['place'],t['properties']['sig']))

print("Total number of quakes:", TotalEvents) 
print("Number of quakes felt by at least 100 people:", TotalFelt)
print("Most felt event:", MostFeltEvent)
print("Most felt count:", MostFeltCount)