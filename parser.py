import json
from datetime import datetime

file = open('raffle.json') 
data = json.load(file)
access = data['entrants']

def getTimestampsMin(list_):
    timestamps = list(d.get('timestamp', 0) for d in list_)
    minT = min(timestamps)
    return datetime.fromtimestamp(minT)
def getTimestampsMax(list_):
    timestamps = list(d.get('timestamp', 0) for d in list_)
    maxT = max(timestamps)
    return datetime.fromtimestamp(maxT)
def filterList(name, list):
    return [element for element in list if element["userName"] == name]
def names (list_):
    names = [sub['userName'] for sub in list_]
    names = list(set(names))
    return names
def fixName (list_):
    name = [sub["userName"] for sub in list_]
    fixedName = name[0].replace('@', '')
    return fixedName
def allTickets(list_):
    tickets = sum(d.get('tickets') for d in list_)
    return tickets
def ticketsPer(subDict):
    realTickets = sum(d.get('tickets', 0) for d in subDict)
    return realTickets
def tickets(subDict):
    currentMax = 10
    if sum(d.get('tickets', 0) for d in subDict) >= currentMax :
        return currentMax
    else:
        return sum(d.get('tickets', 0) for d in subDict)

endfile = open("result.txt", "w")
print("from:", getTimestampsMin(access),"to:", getTimestampsMax(access), file = endfile)
print("total tickets:", allTickets(access), file = endfile)
for name in names(access):
    safeName = fixName(filterList(name, access))
    ticketsToName = tickets(filterList(name, access))
    realTickets = ticketsPer(filterList(name,access))
    print(safeName, "had", realTickets, file= endfile)
    print("!raffle tickets add weekly", safeName, ticketsToName, file = endfile)
endfile.close()
