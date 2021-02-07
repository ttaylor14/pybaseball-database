
# Pulling Data using pybaseball Python Package
# Transforming Data into individual csv files by 
# year and type of statistical Category

# THen combining Data by data Year and by Statistical Category

# Creating a combined Yearly Stat CSV FIle

# And creating a Start to End category list (ie. Batting Stats from 2018-2020)



# was able to get through WSH of 2013 before file got to big to process statcast.
# need to seperate out statcast and do each year first before combining



import pandas as pd
import os



FirstYear = 1950  # First Year to Pull Data
LastYear = 2020   # Last year to Pull Data




def statcast_Data(currentSeason):
    from pybaseball import statcast
    import os
    import pandas as pd

    # StatCast Data Started in 2008
    # Some Features were not added until 2015
    if currentSeason > 2007:

        # Select Start and End Date to Pull data
        Start_Day = "%s-04-01" % currentSeason
        End_Day = "%s-10-03" % currentSeason

        # Create Folder and File Path
        foldername = "data/YearlyData/%s/StatCast/" % currentSeason
        filename_part = "%s_Statcast_" % currentSeason
        print(foldername)

        # Check/Build Directory
        if not os.path.exists(foldername): #adds directory is not already created
            os.mkdir(foldername) 


        # Create Empty StatCast Master File for All teams for each year
        df = pd.DataFrame(list())
        All_Stat_Foldername = 'data/YearlyData/%s/' % currentSeason
        All_Stat_Filename = '%s_All_StatCast.csv' % currentSeason
        All_Stat_Path = (All_Stat_Foldername + All_Stat_Filename)
        df.to_csv(All_Stat_Path)

        #Create Team List to cycle Through
        Team_List = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CWS', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KC', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SD', 'SEA', 'SF', 'STL', 'TB', 'TEX', 'TOR', 'WSH']


        # Loop Through all Teams pulling data from selected dates
        # Saved as individual Team Files
        # Also Saved as 1 master file
        for i in Team_List:

            # Get all data for each team in the current season
            statcast_data = statcast(Start_Day, End_Day, team=i)
                
            # Build File Name for Statcast Data for individual Team
            teamname = "%s.csv" % i        
            filename = (filename_part + teamname)
            statcast_data.to_csv(foldername + filename)

            # Read Master Statcast File for Year
            statcast_data_file_all = pd.read_csv(All_Stat_Path)

            # Add New Team Data to Statcast Year Data
            All_StatCast_File = statcast_data.append(statcast_data_file_all, ignore_index=True)

            # Save new Data to File
            All_StatCast_File.to_csv(All_Stat_Path)

            print(str(currentSeason) + " Statcast Data for : " + str(i) + " : Successful")

    
    print(str(currentSeason) + " All Statcast Data for : Successful")



    print(str(currentSeason) + ": Successful")





# Function Tests

statcast_Data(2018) # Verified Success
print("Successful")