import os 

import csv

votes = []

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:

        votes.append(row[2])

totalvotes = len(votes)

candidatelist = list(set(votes))

results = [(name,votes.count(name)) for name in candidatelist]

sortedresult = sorted(results,key=lambda x: x[1],reverse=True)


print("")

print("Election Results")

print("-------------------------")

print(f"Total Votes: {totalvotes}")

print("-------------------------")

for i in range(len(candidatelist)):

    percent = f"{(int(sortedresult[i][1])/totalvotes * 100):.3f}"

    print(f"{sortedresult[i][0]}: {percent}% ({sortedresult[i][1]})")

print("-------------------------")

print("Winner: " + sortedresult[0][0])

print("-------------------------")

output_path = os.path.join("election_results.txt")

with open(output_path, "w") as txt:

    txt.write("Election Results\n")

    txt.write("-------------------------\n")

    txt.write(f"Total Votes: {totalvotes}\n")

    txt.write("-------------------------\n")

    for i in range(len(candidatelist)):

        percent = f"{(int(sortedresult[i][1])/totalvotes * 100):.3f}"

        txt.write(f"{sortedresult[i][0]}: {percent}% ({sortedresult[i][1]})\n")

    txt.write("-------------------------\n")

    txt.write("Winner: " + sortedresult[0][0] +"\n")

    txt.write("-------------------------")