import pandas as pd
import numpy as np
import os
import csv

file="budget_data.csv"

#define dataframe
budget_df=pd.read_csv(file)

#find total months by counting the amount of months
rows=budget_df.shape[0]
print("Total amount of months is "+str(rows))

#net total of profits
total_profit=budget_df['Profit/Losses'].sum()
print('Total profits for the period is ' + str('$')+str(total_profit))

                  
#define a new dataframe that is profit only
monthly_profits=budget_df["Profit/Losses"]

#calculate month to month change in profit
monthly_profit_change=monthly_profits.diff()        #Kengo's gift

#average change in month to month profit changes
avg_monthly_change=monthly_profit_change.mean()
avg_monthly_change=round(avg_monthly_change)
print("The average change in profits on a month to month basis is " + str("$")+str(avg_monthly_change))

#append the monthly change data to budget_df
budget_df["Monthly Profit Change"]=monthly_profit_change

#find greatest increase in profit (date and amount) over the entire period
max_profit=budget_df.loc[budget_df["Monthly Profit Change"].idxmax()]
print("The greatest increase in profit is from date period "+str(max_profit[0]) + " with an amount of "+str("$") + str(max_profit[1]))


#find the greatest decrease in profit (date and amount) over the entire period
min_profit=budget_df.loc[budget_df["Monthly Profit Change"].idxmin()]
print("The greatest decrease in profit is from date period "+str(min_profit[0]) + " with an amount of "+str("$") + str(min_profit[1]))

#export as text file
results=os.path.join("Analysis", "PyBank.txt")

with open(results, "w") as datafile:
    writer=csv.writer(datafile)
    writer.writerow([str(rows)+ str(total_profit)+ str(avg_monthly_change)+ str(max_profit)+ str(min_profit)])



    

