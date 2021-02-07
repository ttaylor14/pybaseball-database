# pybaseball-database
Pybaseball Database



# Step 1:

Required Python Packages:

- pandas
- pybaseball


# Step 2:

Run file: 
'Baseball-Data.py'

Currently set to run between the years of 1950-2020
- Can easily be adjust at the top of the file

* File takes approximately 1 hour to run as it currently is written



## This file completes the following:

- Creates Data Directories
- Downloads the lahman Database
- Pulls all Battings Stats
- Pulls all Pitching Stats
- Pulls all Team Batting Stats
- Pulls all Team Pitching Stats
- Pulls all Statcast Exit Velocity Data
- Pulls Top Prospect Data
- Pulls Fangraph Batting Data
- Pulls Fangraph Pitching Data
- Pulls Fangraph Team batting Data
- Pulls Fangraphs Team Pitching Data

## Files are organized into folders by year.

Each Year folder contains
- All Batting Stats
- All Pitching Stats
- All Batting and Pitching Stats Combined
- All Team Batting Stats
- All Team Pitching Stats

-After 2007:
- Statcast Exit Velocity Data is added


## Data is also combined into a file containing data from all the selected years

files include:
- All Batting Stats
- All Pitching Stats
- All Combined Stats
- All Exit Velocity Stats
- All FanGraph Stats
- All Team Batting Data
- All Team Pitching Data
- Top Prospect Data


Data to later include:

[ ] - Team Standings (Currently pulled as a long list and needs to be transformed into a DataFrame)

[ ] - Amateur Draft (Code Works, but more research is needed to pull all data) (additional file?)

[ ] - Fielding Data (pybaseball Fielding Code was not working - may need to use Fangraph/lahman)

[ ] - Add fangraph data to each year folder?

[ ] - Possibly add lahman data to each year folder?



# Step 3:

Run file: 
'StatcastPull.py'

* Safe Guard is in place, but Stacast Data began in 2008

This file will pull all statcast data for 1 season

Data is placed in a seperate statcast folder and creates a seperate file for each team
Data is also combined into an All Statcast File for the given year.

This was originally incorporated in the file from Step 2, however, it cause a significant incease in time and memory allocation.

The code is included to combine all statcast files into one historical statcast data file
(However, Memory issues were causing issues)



It is highly recommended to run only a a few years at a time to reduce run time.
Takes approximately 30 minutes to 1 hour per year




# Future Additions/changes

[ ] - Combining Lahman Database data into 1 complete file

[ ] - Creating an additional file to add a single new season to the database and reduce run speed for post 2021 season

[ ] - Investigate columns with mixed types and resolve the issues






