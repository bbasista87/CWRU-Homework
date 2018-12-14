import os

import csv

date = []

pl = []

csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:

        date.append(row[0])

        pl.append((row[1]))

total = 0

for num in pl:

    total = total +float(num)

average = (float(pl[len(pl) - 1]) - float(pl[0]))/(len(date) - 1)

max = float(pl[1]) - float(pl[0])

min = float(pl[1]) - float(pl[0])

for i in range(len(pl) - 1):

    if (float(pl[i + 1]) - float(pl[i])) > max:

        max = float(pl[i + 1]) - float(pl[i])
        
        maxdate = date[i + 1]
    
    elif (float(pl[i + 1]) - float(pl[i])) < min:

        min = float(pl[i + 1]) - float(pl[i])

        mindate = date[i + 1]

print("")

print("Financial Analysis")

print("--------------------------------------------------")

print(f"Total Months: {len(date)}")

print(f"Total: ${total:.0f}")

print(f"Average Change: ${average:.2f}")

print(f"Greatest Increase in Profits: {maxdate} (${max:.0f})")

print(f"Greatest Decrease in Profits: {mindate} (${min:.0f})")

print("")


output_path = os.path.join("financial_analysis.txt")

with open(output_path, "w", newline="") as txt:

    txt.write("Financial Analysis\n")

    txt.write("--------------------------------------------------\n")

    txt.write(f"Total Months: {len(date)}\n")

    txt.write(f"Total: ${total:.0f}\n")

    txt.write(f"Average Change: ${average:.2f}\n")

    txt.write(f"Greatest Increase in Profits: {maxdate} (${max:.0f})\n")

    txt.write(f"Greatest Decrease in Profits: {mindate} (${min:.0f})")