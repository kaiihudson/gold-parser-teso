from slpp import slpp as lua
import json

file = open('RaffleGold.lua')
endfile = open('raffle.json', "w")
print(json.dumps(lua.decode(file.read()), sort_keys=True, indent=2), file= endfile)
endfile.close()
file.close()