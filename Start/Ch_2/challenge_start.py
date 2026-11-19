# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import defaultdict

defdict = defaultdict(lambda: 0)
# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

for feature in data['features']:
    defdict[feature['properties']['type']] +=1

print("Number of events by type:")
for event_type, count in defdict.items():
    print(f"  {event_type}: {count}")
