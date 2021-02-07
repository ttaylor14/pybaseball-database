
# Pulling Data using pybaseball Python Package
# Transforming Data into individual csv files by 
# year and type of statistical Category

# THen combining Data by data Year and by Statistical Category

# Creating a combined Yearly Stat CSV FIle

# And creating a Start to End category list (ie. Batting Stats from 2018-2020)


# Statcast Data Pull was moved to a seperate file


import pandas as pd
import os



FirstYear = 1950  # First Year to Pull Data
LastYear = 2020   # Last year to Pull Data


# Function Creates the Required Directory Tree
# If not Already Created
def create_Dir():
    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists('data/YearlyData'):
        os.mkdir('data/YearlyData')
    if not os.path.exists('data/YearlyData/Lahman'):
        os.mkdir('data/YearlyData/Lahman')
    if not os.path.exists('data/YearlyData/temp'):
        os.mkdir('data/YearlyData/temp')


# Lahman Database Data

from pybaseball.lahman import *
download_lahman() #download the entire lahman database to your current working directory

# a table of all player biographical info and ids
people = people()
people.to_csv('data/YearlyData/Lahman/Lahman_People.csv')


# park id, name, alias, city, state, and country
parks = parks()
parks.to_csv('data/YearlyData/Lahman/Lahman_Parks.csv', sep=',', index=False, encoding='utf-8')


# all star roster data: player, year, team, league, position
allstar = all_star_full()
allstar.to_csv('data/YearlyData/Lahman/Lahman_All_Star.csv', sep=',', index=False, encoding='utf-8')


# each player's games played per position for each season
appearances = appearances()
appearances.to_csv('data/YearlyData/Lahman/Lahman_Appearance.csv', sep=',', index=False, encoding='utf-8')


# manager awards by year
awards_mgr = awards_managers()
awards_mgr.to_csv('data/YearlyData/Lahman/Lahman_Awards_Mgr.csv', sep=',', index=False, encoding='utf-8')


# player awards by year
awards_player = awards_players()
awards_player.to_csv('data/YearlyData/Lahman/Lahman_Awards_Player.csv', sep=',', index=False, encoding='utf-8')


# vote shares by year for manager awards 
award_share_mgr = awards_share_managers()
award_share_mgr.to_csv('data/YearlyData/Lahman/Lahman_Awards_Share_Mgr.csv', sep=',', index=False, encoding='utf-8')


# vote shares by year for player awards 
award_share_player = awards_share_players()
award_share_player.to_csv('data/YearlyData/Lahman/Lahman_Awards_Share_Player.csv', sep=',', index=False, encoding='utf-8')


# batting stats by year, regular season
batting = batting()
batting.to_csv('data/YearlyData/Lahman/Lahman_Batting.csv', sep=',', index=False, encoding='utf-8')


# batting stats by year, post season
batting_post = batting_post()
batting_post.to_csv('data/YearlyData/Lahman/Lahman_Batting_Post.csv', sep=',', index=False, encoding='utf-8')


# the college a player played at each year
college_playing = college_playing()
college_playing.to_csv('data/YearlyData/Lahman/Lahman_College_Playing.csv', sep=',', index=False, encoding='utf-8')


# fielding stats by year 
fielding = fielding()
fielding.to_csv('data/YearlyData/Lahman/Lahman_Fielding.csv', sep=',', index=False, encoding='utf-8')


# games played in left, center, right field 
fielding_of = fielding_of()
fielding_of.to_csv('data/YearlyData/Lahman/Lahman_Fielding_OF.csv', sep=',', index=False, encoding='utf-8')


# LF/CF/RF splits
fielding_of_split = fielding_of_split()
fielding_of_split.to_csv('data/YearlyData/Lahman/Lahman_Fielding_OF_Split.csv', sep=',', index=False, encoding='utf-8')


# postseason fielding 
fielding_post = fielding_post()
fielding_post.to_csv('data/YearlyData/Lahman/Lahman_Fielding_Post.csv', sep=',', index=False, encoding='utf-8')


# hall of fame voting by year 
hall_of_fame = hall_of_fame()
hall_of_fame.to_csv('data/YearlyData/Lahman/Lahman_Hall_Of_Fame_Vote.csv', sep=',', index=False, encoding='utf-8')


# home game attendance by park by year 
home_games = home_games()
home_games.to_csv('data/YearlyData/Lahman/Lahman_Home_Game_Attendance.csv', sep=',', index=False, encoding='utf-8')


# managers by team and year
managers = managers()
managers.to_csv('data/YearlyData/Lahman/Lahman_Managers.csv', sep=',', index=False, encoding='utf-8')


# split season managers data
managers_half = managers_half()
managers_half.to_csv('data/YearlyData/Lahman/Lahman_Managers_Half.csv', sep=',', index=False, encoding='utf-8')


# historical player pitching stats
pitching = pitching()
pitching.to_csv('data/YearlyData/Lahman/Lahman_Pitching.csv', sep=',', index=False, encoding='utf-8')


# postseason pitching stats
pitching_post = pitching_post()
pitching_post.to_csv('data/YearlyData/Lahman/Lahman_Pitching_Post.csv', sep=',', index=False, encoding='utf-8')


# salary data
salaries = salaries()
salaries.to_csv('data/YearlyData/Lahman/Lahman_Salaries.csv', sep=',', index=False, encoding='utf-8')


# schools attended by each player
schools = schools()
schools.to_csv('data/YearlyData/Lahman/Lahman_Schools.csv', sep=',', index=False, encoding='utf-8')


# playoff series winners and losers 
series_post = series_post()
series_post.to_csv('data/YearlyData/Lahman/Lahman_Series_Post.csv', sep=',', index=False, encoding='utf-8')


# data on teams by year: record, division, stadium, attendance, etc
teams = teams()
teams.to_csv('data/YearlyData/Lahman/Lahman_Teams.csv', sep=',', index=False, encoding='utf-8')


# current and historical franchises, whether they're still active, and their ids
teams_franchises = teams_franchises()
teams_franchises.to_csv('data/YearlyData/Lahman/Lahman_Team_Franchises.csv', sep=',', index=False, encoding='utf-8')


# split season data for teams
teams_half = teams_half()
teams_half.to_csv('data/YearlyData/Lahman/Lahman_Teams_Half.csv', sep=',', index=False, encoding='utf-8')







# Pull Data from a given year for each statistical category and build temp files for use
def yearGrab(currentSeason):

    # Batting Stats
    from pybaseball import batting_stats
 
    BattingStats_Year = batting_stats(currentSeason, qual=1)
    # print(BattingStats_Year.head()) # Test
    BattingStats_Year.to_csv('data/YearlyData/temp/bstats.csv')

    import pybaseball

    #Team Batting Stats
    BattingStats_Team_Year = pybaseball.team_batting(currentSeason)
    BattingStats_Team_Year.to_csv('data/YearlyData/temp/team_bstats.csv')



    # Pitching Stats
    from pybaseball import pitching_stats

    PitchingStats_Year = pitching_stats(currentSeason)
    # print(PitchingStats_Year.head()) # Test
    PitchingStats_Year.to_csv('data/YearlyData/temp/pstats.csv')

    print(str(currentSeason) + " : Stats Grab: Successful")
    
    # Team Pitching Stats
    PitchingStats_Team_Year = pybaseball.team_pitching(currentSeason)
    PitchingStats_Team_Year.to_csv('data/YearlyData/temp/team_pstats.csv')


    """
    # Year Standings
    if currentSeason >=1969:
        from pybaseball import standings
        # get the end-of-season division standings for each season
        Standings = standings(currentSeason)
        Standings.insert(0, 'Season', currentSeason)
        Standings.to_csv('data/YearlyData/temp/team_standings.csv')
    """

    """
    # Amateur Draft Data
    if currentSeason >= 1965:

        from pybaseball import amateur_draft

        # Get amateur Draft Results
        Number_Rounds = 30
        RoundRange = list(range(1, Number_Rounds + 1))
        for i in RoundRange:
            #Pull season draft data 1 round at a time
            Amateur_Draft = amateur_draft(currentSeason, i)
            #Add Draft Year
            Amateur_Draft.insert(0, 'Draft_Year', currentSeason)

            # print(Amateur_Draft.head()) # Test

            # Read file with all draft files so far
            A_Draft = pd.read_csv('data/YearlyData/temp/amateur_draft.csv') 
            # Add New Round
            A_Draft = A_Draft.append(Amateur_Draft, ignore_index=True)
            #Save new round to File
            A_Draft.to_csv('data/YearlyData/temp/amateur_draft.csv', sep=',', index=False, encoding='utf-8')
        """


    # Exit Veolocity Data

    from pybaseball import statcast_batter_exitvelo_barrels

    Exit_Velocity = statcast_batter_exitvelo_barrels(currentSeason)
    Exit_Velocity.insert(0, 'Season', currentSeason)
    Exit_Velocity.to_csv('data/YearlyData/temp/statcast_exit_velocity.csv')


    # FanGraph Data
    import pybaseball

    # Individual Batting Stats
    fan_bat = pybaseball.batting_stats(currentSeason)
    fan_bat.to_csv('data/YearlyData/temp/fan_bat.csv')


    # Individual Pitching Stats
    fan_pit = pybaseball.pitching_stats(currentSeason)
    fan_pit.to_csv('data/YearlyData/temp/fan_pit.csv')

    # Team Batting Stats
    fan_team_bat = pybaseball.team_batting(currentSeason)
    fan_team_bat.to_csv('data/YearlyData/temp/fan_team_bat.csv')

    # Team Pitching Stats
    fan_team_pit = pybaseball.team_pitching(currentSeason)
    fan_team_pit.to_csv('data/YearlyData/temp/fan_team_pit.csv')




    from pybaseball import top_prospects

    # Get top overall prospects leaguewide
    topProspects = top_prospects()
    topProspects.to_csv('data/YearlyData/Top_Prospects.csv')




# Combine all Stat Categories into a single Year csv (ie. COmbine Batting, pitching, fielding...)
def combineYear(currentSeason):

    bstats = pd.read_csv('data/YearlyData/temp/bstats.csv')
    pstats = pd.read_csv('data/YearlyData/temp/pstats.csv')

    bstats = bstats.add_suffix('_bat')
    pstats = pstats.add_suffix('_pit')
    # print(pstats.head())

    #Combine CSV
    FullYearStats = pd.merge(bstats, pstats, left_on=['Name_bat', 'Age_bat', 'Team_bat'], right_on=['Name_pit', 'Age_pit', 'Team_pit'], how='outer', suffixes=('_bat', '_pit'))
    FullYearStats.to_csv('data/YearlyData/temp/YearStats.csv')


    # Combine Team batting and Pitching Data

    team_bstats = pd.read_csv('data/YearlyData/temp/team_bstats.csv')
    team_pstats = pd.read_csv('data/YearlyData/temp/team_pstats.csv')

    team_bstats = team_bstats.add_suffix('_bat')
    team_pstats = team_pstats.add_suffix('_pit')
    # print(pstats.head())

    #Combine CSV
    FullYearTeamStats = pd.merge(team_bstats, team_pstats, left_on=['Team_bat', 'Season_bat'], right_on=['Team_pit', 'Season_pit'], how='outer')
    FullYearTeamStats.to_csv('data/YearlyData/temp/YearTeamStats.csv')


    print(str(currentSeason) + " : Year of Stats: Successful")
  



# Combining Like Stats into a Multi-Year CSV (ie. All Batting Stats for a given year span)
def combineStats(currentSeason):

    ## ALL Stats
    all_stats = pd.read_csv('data/YearlyData/temp/YearStats.csv') 
    stats_all = pd.read_csv('data/YearlyData/All_Stats.csv')

    All_Stats = stats_all.append(all_stats, ignore_index=True)
    All_Stats.to_csv('data/YearlyData/All_Stats.csv', sep=',', index=False, encoding='utf-8')


    ## Batting Stats
    bstats = pd.read_csv('data/YearlyData/temp/bstats.csv')
    batting_stats_all = pd.read_csv('data/YearlyData/All_Batting_Stats.csv')

    All_Bat = batting_stats_all.append(bstats, ignore_index=True)
    All_Bat.to_csv('data/YearlyData/All_Batting_Stats.csv', sep=',', index=False, encoding='utf-8')

    #Team Batting
    team_bstats = pd.read_csv('data/YearlyData/temp/team_bstats.csv')
    team_batting_stats_all = pd.read_csv('data/YearlyData/All_Team_Batting_Stats.csv')

    All_Team_Bat = team_batting_stats_all.append(team_bstats, ignore_index=True)
    All_Team_Bat.to_csv('data/YearlyData/All_Team_Batting_Stats.csv', sep=',', index=False, encoding='utf-8')


    ## Pitching Stats
    pstats = pd.read_csv('data/YearlyData/temp/pstats.csv') 
    pitching_stats_all = pd.read_csv('data/YearlyData/All_Pitching_Stats.csv')

    All_Pit = pitching_stats_all.append(pstats, ignore_index=True)
    All_Pit.to_csv('data/YearlyData/All_Pitching_Stats.csv', sep=',', index=False, encoding='utf-8')

    ## Team Pitching Stats
    team_pstats = pd.read_csv('data/YearlyData/temp/team_pstats.csv') 
    team_pitching_stats_all = pd.read_csv('data/YearlyData/All_Team_Pitching_Stats.csv')

    All_Team_Pit = team_pitching_stats_all.append(team_pstats, ignore_index=True)
    All_Team_Pit.to_csv('data/YearlyData/All_Team_Pitching_Stats.csv', sep=',', index=False, encoding='utf-8')

    """
    if currentSeason >=1969:
        ## Team Standings Stats
        Standings = pd.read_csv('data/YearlyData/temp/team_standings.csv') 
        Standings_all = pd.read_csv('data/YearlyData/All_Standings.csv')

        All_Stand = Standings_all.append(Standings, ignore_index=True)
        All_Stand.to_csv('data/YearlyData/All_Standings.csv', sep=',', index=False, encoding='utf-8')
    """
    """
    if currentSeason >= 1965:
        ## Amateur Draft Data for first 30 rounds each year available
        a_draft = pd.read_csv('data/YearlyData/temp/amateur_draft.csv') 
        A_Draft_all = pd.read_csv('data/YearlyData/All_Amateur_Draft.csv')

        All_A_Draft = A_Draft_all.append(a_draft, ignore_index=True)
        All_A_Draft.to_csv('data/YearlyData/All_Amateur_Draft.csv', sep=',', index=False, encoding='utf-8')
    """

    ## StatCast Exit Velocity Data
    e_velo = pd.read_csv('data/YearlyData/temp/statcast_exit_velocity.csv') 
    E_Velo_all = pd.read_csv('data/YearlyData/All_Exit_Velocity.csv')

    All_E_Velo = E_Velo_all.append(e_velo, ignore_index=True)
    All_E_Velo.to_csv('data/YearlyData/All_Exit_Velocity.csv', sep=',', index=False, encoding='utf-8')


    ## Fangraph Data

    ## Fangraph Player Batting
    fan_bat = pd.read_csv('data/YearlyData/temp/fan_bat.csv') 
    fan_bat_all = pd.read_csv('data/YearlyData/All_Fangraph_Batting_Stats.csv')

    All_fan_bat = fan_bat_all.append(fan_bat, ignore_index=True)
    All_fan_bat.to_csv('data/YearlyData/All_Fangraph_Batting_Stats.csv', sep=',', index=False, encoding='utf-8')

    ## Fangraph Player Pitching
    fan_pit = pd.read_csv('data/YearlyData/temp/fan_pit.csv') 
    fan_pit_all = pd.read_csv('data/YearlyData/All_Fangraph_Pitching_Stats.csv')

    All_fan_pit = fan_pit_all.append(fan_pit, ignore_index=True)
    All_fan_pit.to_csv('data/YearlyData/All_Fangraph_Pitching_Stats.csv', sep=',', index=False, encoding='utf-8')

    ## Fangraph Team Batting
    fan_team_bat = pd.read_csv('data/YearlyData/temp/fan_team_bat.csv') 
    fan_team_bat_all = pd.read_csv('data/YearlyData/All_Fangraph_Team_Batting_Stats.csv')

    All_fan_team_bat = fan_team_bat_all.append(fan_team_bat, ignore_index=True)
    All_fan_team_bat.to_csv('data/YearlyData/All_Fangraph_Team_Batting_Stats.csv', sep=',', index=False, encoding='utf-8')

    ## Fangraph Team Pitching
    fan_team_pit = pd.read_csv('data/YearlyData/temp/fan_team_pit.csv') 
    fan_team_pit_all = pd.read_csv('data/YearlyData/All_Fangraph_Team_Pitching_Stats.csv')

    All_fan_team_pit = fan_team_pit_all.append(fan_team_bat, ignore_index=True)
    All_fan_team_pit.to_csv('data/YearlyData/All_Fangraph_Team_Pitching_Stats.csv', sep=',', index=False, encoding='utf-8')








    print(str(currentSeason) + " : Added to Combined Stats: Successful")
  


# File is used to Clear the All Stats csv Files prior to adding new information
# This prevent Duplication of the all_Stat Files append
def Clear_CSV():

    df = pd.DataFrame(list())
    df.to_csv('data/YearlyData/temp/team_standings.csv')
    df.to_csv('data/YearlyData/temp/amateur_draft.csv')
    df.to_csv('data/YearlyData/temp/statcast_exit_velocity.csv')
    df.to_csv('data/YearlyData/temp/YearStats.csv')
    df.to_csv('data/YearlyData/temp/bstats.csv')
    df.to_csv('data/YearlyData/temp/team_bstats.csv')
    df.to_csv('data/YearlyData/temp/pstats.csv')
    df.to_csv('data/YearlyData/temp/team_pstats.csv')
    df.to_csv('data/YearlyData/temp/YearTeamStats.csv')
    df.to_csv('data/YearlyData/All_Stats.csv')
    df.to_csv('data/YearlyData/All_Batting_Stats.csv')
    df.to_csv('data/YearlyData/All_Pitching_Stats.csv')
    df.to_csv('data/YearlyData/All_Fangraph_Batting_Stats.csv')
    df.to_csv('data/YearlyData/All_Fangraph_Pitching_Stats.csv')
    df.to_csv('data/YearlyData/All_Fangraph_Team_Batting_Stats.csv')
    df.to_csv('data/YearlyData/All_Fangraph_Team_Pitching_Stats.csv')
    df.to_csv('data/YearlyData/All_Standings.csv')
    df.to_csv('data/YearlyData/All_Amateur_Draft.csv')
    df.to_csv('data/YearlyData/All_Exit_Velocity.csv')
    df.to_csv('data/YearlyData/All_Team_Pitching_Stats.csv')
    df.to_csv('data/YearlyData/All_Team_Batting_Stats.csv')

    print("Files Cleared: Successful")
  


def Create_Stat_Files():

    global LastYear
    global FirstYear

    create_Dir() # Creates Directories
    Clear_CSV()  # Creates Empty csv Files and Clear CSV

    # Creates Year Range to Rotate data Pull Through
    yearRange = list(range(FirstYear, LastYear + 1))
    



    # print(yearRange)
    for x in yearRange:

        # print(X)

        #Grab Year Data
        yearGrab(x)
        # Combine Year Data
        combineYear(x)
        # Combine Data by Stats
        combineStats(x)


        foldername = "data/YearlyData/%s/" % x

        if not os.path.exists(foldername): #adds directory is not already created
            os.mkdir(foldername) 
            
        R = pd.read_csv('data/YearlyData/temp/YearStats.csv')
        filename = "%s_Combined.csv" % x
        R.to_csv(foldername + filename)

        R = pd.read_csv('data/YearlyData/All_Batting_Stats.csv')
        filename = "%s_Batting_Stats.csv" % x
        R.to_csv(foldername + filename)

        R = pd.read_csv('data/YearlyData/All_Team_Batting_Stats.csv')
        filename = "%s_Team_Batting_Stats.csv" % x
        R.to_csv(foldername + filename)

        R = pd.read_csv('data/YearlyData/All_Pitching_Stats.csv')
        filename = "%s_Pitching_Stats.csv" % x
        R.to_csv(foldername + filename)


        R = pd.read_csv('data/YearlyData/All_Team_Pitching_Stats.csv')
        filename = "%s_Team_Pitching_Stats.csv" % x
        R.to_csv(foldername + filename)
        """
        if x >= 1969:
            R = pd.read_csv('data/YearlyData/team_Standings.csv')
            filename = "%s_Standings.csv" % x
            R.to_csv(foldername + filename)
        """
        """
        if x >= 1965:
            R = pd.read_csv('data/YearlyData/temp/amateur_draft.csv')
            filename = "%s_Amateur_Draft.csv" % x
            R.to_csv(foldername + filename)
        """


        """
        R = pd.read_csv('data/YearlyData/fan_bat.csv')
        filename = "%s_Fangraph_Batting.csv" % x
        R.to_csv(foldername + filename)

        R = pd.read_csv('data/YearlyData/fan_bpit.csv')
        filename = "%s_Fangraph_Pitching.csv" % x
        R.to_csv(foldername + filename)

        R = pd.read_csv('data/YearlyData/fan_team_bat.csv')
        filename = "%s_Fangraph_Team_Batting.csv" % x
        R.to_csv(foldername + filename)

        R = pd.read_csv('data/YearlyData/fan_team_pit.csv')
        filename = "%s_Fangraph_Team_Pitching.csv" % x
        R.to_csv(foldername + filename)
        """


        print(str(x) + ": Successful")





# Function Tests
# Clear_CSV()         # Verified Succes
# yearGrab(2017)      # Verified Success
# combineYear(2017)   # Verified Success
# combineStats(2017)  # Verified Success
# print("Successful")




Create_Stat_Files()
print("Successful")