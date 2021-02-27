import pandas as pd
import numpy as np
import os
import csv

file="election_data.csv"

#define dataframe
election_df=pd.read_csv(file)

#total number of votes cast
total_votes=election_df.shape[0]
print("Total amount of votes cast is "+str(total_votes))

#A complete list of candidates who received votes (column index 2)
candidates_df=election_df["Candidate"].unique()
print("The candidates were " +str(candidates_df))

#percentage of votes each candidate won
candidate_count_df=election_df.groupby(["Candidate"]).count()
print(candidate_count_df)
candidate_percentage=round((candidate_count_df/total_votes)*100)
print(candidate_percentage)

#rearrange dataframe
# election_results_df=election_df[["Candidate", "candidate_percentage","candidate_count"]]
# print(election_results_.head())

#winner is the candidate with max counts
winner=candidate_count_df.max()

#export as text file
results=os.path.join("Analysis", "PyPoll.txt") 

with open(results, "w") as datafile:
    writer=csv.writer(datafile)

    writer.writerow([str(total_votes)])
    writer.writerow([str(candidates_df)])
    writer.writerow([str(candidate_count_df)])
    writer.writerow([str(candidate_percentage)])
    writer.writerow([str(winner)])
    
    
   







