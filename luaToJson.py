from slpp import slpp as lua
import json

file = open('RaffleGold.lua')
rawJSON= lua.decode(file.read())
# print(rawJSON)
data = rawJSON
access = data['Default']['@KaiiHudson']['$AccountWide']['prizes']

def fixElements(any):
    if type(any) is list:
        return [fixElements(x) for x in any]
    if type(any) is not dict:
        return any
    keyList = list(any.keys())
    var = 1
    fixable = True
    for x in range(len(keyList)):
        if not var + x in keyList:
            fixable = False
            break
    if not fixable:
        return { k: fixElements(v) for k,v in any.items() }
    else:
        return list(any.values())

fixedJSON = fixElements(access)
endfile = open('raffle.json', "w")
print(json.dumps(fixedJSON, sort_keys=True, indent=2), file= endfile)
file.close()
endfile.close()