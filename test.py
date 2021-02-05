from pybaseball import standings
import pandas as pd


currentSeason = 1970

if currentSeason >=1969:
    from pybaseball import standings
    # get the end-of-season division standings for each season
    Standings = standings(currentSeason)
    print(Standings)
    Standings.insert(1, currentSeason)
    print(Standings.head())
