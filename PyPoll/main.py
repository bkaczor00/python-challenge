import csv
import os

path = "election_data.csv"

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    
    print("Election Results")
    print("--------------------")
    
    header = next(csv_reader)
    
    row_count = sum(1 for row in file)
    print("total votes: "+ str(row_count))
    print("---------------------") 


with open(path, "r") as file:
    csv_reader = csv.reader(file)
    
    header = next(csv_reader)
    
    candidate_list = []
    for row in csv_reader:
        candidate_list.append(row[2])
        
    candidate_dict = {}
    for row in set(candidate_list):
        candidate_dict.update({row:0})
        
    for row in candidate_list:
        candidate_dict[row] +=1


for (key, value) in candidate_dict.items():
    
    percentage = candidate_dict[key] / (row_count)
    print_percent = print(key,"%", round(percentage*100),"(",value,")")
    

print("---------------------")

for (key, value) in candidate_dict.items():
  
    max_key = max(candidate_dict, key=candidate_dict. get)

    print("winner:", max_key)
    
    break
    
election_results = os.path.join("..", "anaylsis", "electionresults.txt")
with open("electionresults", 'w') as poll_data:
    poll_data.writelines("       Election Results    \n")
    poll_data.writelines("---------------------------\n")
    poll_data.writelines(f"total votes: {row_count}\n")
    poll_data.writelines("---------------------------\n")
    poll_data.writelines(f"{key} % {round(percentage*100)} ({value}) \n")
    poll_data.writelines("---------------------------\n")
    poll_data.writelines(f"winner: {max_key}")