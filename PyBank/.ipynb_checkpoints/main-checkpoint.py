import csv
import os
                              
with open ('budget_data.csv',"r") as file:
    csv_reader = csv.reader(file, delimiter=",")
                              
    header = next(csv_reader)
    
    print("Financial Analysis")
    print("------------------")
    
    row_count = sum(1 for row in file) 
    print ("total months: ", row_count)
    
    
with open ('budget_data.csv',"r") as file:
    csv_reader = csv.reader(file, delimiter=",")

    header = next(csv_reader)
    
    total_profit=0
    for row in csv_reader:  
        total_profit += int(row[1])
                              
    print("total profit: $",total_profit)
    

with open ('budget_data.csv',"r") as file:
    csv_reader = csv.reader(file, delimiter=",")
    
    header = next(csv_reader)
    profit = []
    profit_change = []
    date =[]
    
    for row in csv_reader:
        profit.append(float(row[1]))
        date.append(row[0])
        
    for row in range(1,len(profit)):
        profit_change.append(profit[row] - profit[row-1])   
        avg_profit_change = sum(profit_change)/len(profit_change)

        max_profit_change = max(profit_change)

        min_profit_change = min(profit_change)

    max_profit_change_date = str(date[profit_change.index(max(profit_change))])
    min_profit_change_date = str(date[profit_change.index(min(profit_change))])


    print("average change: $", float(avg_profit_change))
    print("greatest increase in profit: ", max_profit_change_date,"($", max_profit_change,")")
    print("greatest decrease in profit: ", min_profit_change_date,"($", min_profit_change,")")

financial_analysis = os.path.join("..", "anaylsis", "financialanalysis.txt")  
with open("fiancial_analysis", 'w') as financial_data:
    financial_data.writelines("       Financial Analysis    \n")
    financial_data.writelines("---------------------------\n")
    financial_data.writelines(f"total months: {row_count}\n")
    financial_data.writelines(f"total profit: ${total_profit}\n")
    financial_data.writelines(f"average change: ${float(avg_profit_change)}\n")
    financial_data.writelines(f"greatest increase in profit: {max_profit_change_date} (${max_profit_change})\n")
    financial_data.writelines(f"greatest decrease in profit: {min_profit_change_date} (${min_profit_change})")