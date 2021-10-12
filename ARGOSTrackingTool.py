#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2021
#--------------------------------------------------------------

#Create a path variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Create two empty dictionaries
date_dict = {}
coord_dict = {}

#Iterate through all lines in linelist
for lineString in line_list:
    if lineString[0] in ("#",'u'): continue

    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract the items in list into variables
    record_id = lineData[0]  # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    ob_lc = lineData[4]      # Observation Location Class
    obs_lat = lineData[6]    # Observation Latitude
    obs_lon = lineData[7]    # Observation Longitude
    
    print(f"Record {record_id} indicated Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
    date_dict[record_id] = obs_date
    coord_dict[record_id] = (obs_lat,obs_lon)

