# Import
import os
import csv
from pathlib import Path

# File
Py_Poll = Path("D:\CODE\Homework3\Python-Challenge\Resources\Election_Data.csv")

# Define what we need to find
Votes_For_Khan = 0
Votes_For_Li = 0
Votes_For_Correy = 0
Votes_For_Otooley = 0
Total_Votes = 0

# Open
with open(Py_Poll,newline="", encoding="utf-8") as Elections:
    csvreader = csv.reader(Elections,delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        # Total Votes 
        Total_Votes +=1
        # Khan
        if row[2] == "Khan":
            Votes_For_Khan +=1
        # Li
        elif row[2] == "Li":
            Votes_For_Li +=1
        # Correy
        elif row[2] == "Correy":
            Votes_For_Correy +=1
        # Otooley
        elif row[2] == "O'Tooley":
            Votes_For_Otooley +=1
# Dictionaries 
Candidates = ["Khan", "Li", "Correy", "O'Tooley"]
Votes_Per = ["Votes_For_Khan","Votes_For_Li","Votes_For_Correy","Votes_For_Otooley"]
Candidates_And_Votes_Per = dict(zip(Candidates,Votes_Per))
Winner = max(Candidates_And_Votes_Per, Winner=Candidates_And_Votes_Per.get)

# Analysis
Percent_For_Khan = (Votes_For_Khan/Total_Votes) *100
Percent_For_Li = (Votes_For_Li/Total_Votes) *100
Percent_For_Correy = (Votes_For_Correy/Total_Votes) *100
Percent_For_Otooley = (Votes_For_Otooley/Total_Votes) *100

# Print
print(f"Election Results")
print(f"--------------------")
print(f"Total Votes: {Total_Votes}")
print(f"--------------------")
print(f"Khan: {Percent_For_Khan:.3f}% ({Votes_For_Khan})")
print(f"Li: {Percent_For_Li:.3f}% ({Votes_For_Li})")
print(f"Correy: {Percent_For_Correy:.3f}% ({Votes_For_Correy})")
print(f"O'Tooley: {Percent_For_Otooley:.3f}% ({Votes_For_Otooley})")
print(f"--------------------")
print(f"Winner: {Winner}")
print(f"--------------------")

# Export
Export_File = Path("D:\CODE\Homework3\Python-Challenge\Resources\Election_Data_Results.txt")
with open(Export_File,"w") as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"--------------------")
    file.write("\n")
    file.write(f"Total Votes: {Total_Votes}")
    file.write("\n")
    file.write(f"--------------------")
    file.write("\n")
    file.write(f"Khan: {Percent_For_Khan:.3f}% ({Votes_For_Khan})")
    file.write("\n")
    file.write(f"Li: {Percent_For_Li:.3f}% ({Votes_For_Li})")
    file.write("\n")
    file.write(f"Correy: {Percent_For_Correy:.3f}% ({Votes_For_Correy})")
    file.write("\n")
    file.write(f"O'Tooley: {Percent_For_Otooley:.3f}% ({Votes_For_Otooley})")
    file.write("\n")
    file.write(f"--------------------")
    file.write("\n")
    file.write(f"Winner: {Winner}")
    file.write("\n")
    file.write(f"--------------------")


    
    



