# gold-parser-teso
## Dependencies for python
- [slpp](https://github.com/SirAnthony/slpp)

## Addons Needed 
    raffle gold
## How To run it
**You need python 3.8.5 or later to run it**
### rafflegold
1. update your guild bank history until you see the first **10 days** in the mix, once its updated, you should be able to run the rafflegold Addon
2. type in chat `/rafflegold` or navigate via the addons menu
3. run a raffle from the last raffle date to the current date, make sure the entry cost is set up right and verify that no exemptions are being made
4. **RUN THE RAFFLE**
5. go to `%username%/Documents/ElderScrolls/live/SavedVariables` and copy the `RaffleGold.lua` file
### running the script
0. copy the `RaffleGold.lua`
   - in the file be sure to delete the line `RaffleGold_SavedVars =` otherwise the script will fail
1. run `luatoJson`
   - raffle.json should be created
2. run `parser`
    - results.txt should be created
3. check the results on the txt file
## Pasting the results on discord

Format is as follows: 
- paste the first 2 lines, those are the limits to the operation
- paste the command into the raffle-bot channel
- once the raffle has been loaded in, the rest of the instructions are in that channel