# Import
import os
import csv
from pathlib import Path
# File
Py_Bank = Path("D:\CODE\Homework3\Python-Challenge\Resources")
with open(Py_Bank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    Header = next(csvreader)

# Lists
Total_Months = []
Total_Profit = []
Monthly_Change = []

# Open File / Append
for row in csvreader:
        Total_Months.append(row[0])
        Total_Profit.append(row[1])
for number in range(len(Total_Profit)-1):
     Monthly_Change.appennd(Total_Profit[number+1]-Total_Profit[number])

# Greatest profit increase / Greatest loss decrease months
Greatest_Profit_Increase = max(Monthly_Change)
Greatest_Loss_Decrease = min(Monthly_Change)
Greatest_Increase = Monthly_Change.index(max(Monthly_Change)) + 1
Greatest_Decrease = Monthly_Change.index(min(Monthly_Change)) + 1

# Print
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {len(Total_Months)}")
print(f"Total: ${sum(Total_Profit)}")
print(f"Average Change: (sum(Monthly_Change)/len(Monthly_Change)")
print(f"Greatest Increase in Profits: {Total_Months[Greatest_Increase]} (${(str(Greatest_Profit_Increase))})")
print(f"Greatest Decrease in Profits: {Total_Months[Greatest_Decrease]} (${(str(Greatest_Loss_Decrease))})")

# Export
Text_File = Path("Python-Challenge", "Analysis", "Final_Analysis.txt")
with open(Text_File,"w") as file:


    # Print to Text
    file.write("Financial Analysis")
    file.write("\n")
    file.write("-----------------------")
    file.write("\n")
    file.write(f"Total Months: {len(Total_Months)}")
    file.write("\n")
    file.write(f"Total: ${sum(Total_Profit)}")
    file.write("\n")
    file.write(f"Average Change: (sum(Monthly_Change)/len(Monthly_Change)")
    file.write(f"Greatest Increase in Profits: {Total_Months[Greatest_Increase]} (${(str(Greatest_Profit_Increase))})")
    file.write(f"Greatest Decrease in Profits: {Total_Months[Greatest_Decrease]} (${(str(Greatest_Loss_Decrease))})")



