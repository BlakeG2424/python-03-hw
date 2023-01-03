# import dependencies
import os
import csv

# declare variables
total_votes = 0
candidate = []
candidate_list = []
candidate_votes = {}
most_votes = 0
winner = ""


# path to collect data and output to analysis file
election_data_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "output.txt")

# open and read csv and header
with open(election_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # start loop through rows, find total votes/candidate name
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        # add candidates to list and track eachs count
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes[candidate] = 0

        # add a vote to the candidate's count
        candidate_votes[candidate] = candidate_votes[candidate] + 1

with open(output_path, "w") as text:


    # print election results to terminal
    election_results = (
            f"\n\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes}\n"
            f"-------------------------\n")
    print(election_results)
    text.write(election_results)


    # find candidate percent counts
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percent = float(votes)/float(total_votes) * 100

        # find winner
        if (votes > most_votes):
            most_votes = votes
            winner = candidate

        # create each candidate's vote count and vote percentage
        results = f"{candidate}: {vote_percent:.3f}% ({votes})\n"

        # print results to terminal
        print(results)
        text.write(results)

        # print winner to terminal
        winning_candidate_name = (
            f"-------------------------\n"
            f"Winner: {winner}\n"
            f"-------------------------\n")
    print(winning_candidate_name)
    text.write(winning_candidate_name)
