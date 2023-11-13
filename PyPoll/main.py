import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "output_PyPoll.csv")
# Initializing varaibles used in the code
output_map = {}
diff_map = {}
i = 0
percent_vote = 0
winner = ""
# Read the csv file election_data.csv
# Create a new dictionary with key = candidate names ; value = list of votes for each candidate
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        if(row[2] in output_map):
            # print(f'row [2] - {row[2]}')
            output_map[row[2]].append(int(row[0]))
        else :
            vote_list = []
            vote_list.append(int(row[0]))
            output_map.update({row[2]:vote_list})
        i += 1
    

total_votes = i

# Write the results to a text file
with open(output_path, "w") as output_file:
    output_file.write("Election Results\n")
    print("Election Results")
    output_file.write("-------------------------\n")
    print("-------------------------")
    output_file.write(f'Total Votes: {total_votes}\n')
    print(f'Total Votes: {total_votes}\n')
    output_file.write("-------------------------\n")
    print("-------------------------")
    # Iterate over the map created earlier to find percentage vote for each candidate and the winner
    for vote in output_map:
        percentage_vote = round((len(output_map[vote])/total_votes)*100,3)
        if(percentage_vote > percent_vote):
            percent_vote = percentage_vote
            winner = vote
        output_file.write(f'{vote}: {percentage_vote}% ({len(output_map[vote])})\n')
        print(f'{vote}: {percentage_vote}% ({len(output_map[vote])})\n')
    output_file.write("-------------------------\n")
    print("-------------------------")
    output_file.write(f'Winner: {winner}\n')
    print(f'Winner: {winner}')
    output_file.write("-------------------------")
    print("-------------------------")