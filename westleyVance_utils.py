"""
Westley Vance
Week 1 - P1: Create a New Python Module (Company Byline)

This module provides a reusable byline for the author's services. 

The goal of this module is to showcases 'Vance Analytics' 
superb skills in the world of consulting and analytics.
"""

import math
import statistics

def byline():
  #variable list
  company_name: str = "Vance Analytics"
  company_description: str = "Knock off food chain consulting firm"
  owner: str = "Westley Vance"
  has_cool_owner: bool = True
  accounts: list = ['MarkDonalds', 'ChickFillets', 'DairyQuans',\
                    'BrugerKings', 'tacoShells', 'ChapOtles']
  account_profits: list = [30000, 40000 , 10000 , 20000 , 500000 , 250000]
  account_With_Profit: str = ""
  yearly_income: float = sum(account_profits)
  yearly_expenses: float = 150000 # fixed cost
  yearly_profit: float = yearly_income - yearly_expenses

  #I coppied your list & variable names for this portion
  smallest = min(account_profits)
  s_index = account_profits.index(smallest)
  largest = max(account_profits)
  l_index = account_profits.index(largest)
  total = sum(account_profits)
  count = len(account_profits)
  mean = statistics.mean(account_profits)
  mode = statistics.mode(account_profits)
  median = statistics.median(account_profits)
  standard_deviation = statistics.stdev(account_profits)

  #Gives statistical info about our fake accounts
  stats_string: str = f"""
Descriptive Statistics for account profits:
  Smallest: ${round(float(smallest),2)} ({accounts[s_index]})
  Largest: ${round(float(largest),2)} ({accounts[l_index]})
  Total: ${round(float(total),2)}
  Count: {count} accounts
  Mean: ${round(mean,2)}
  Mode: ${round(float(mode),2)}
  Median: ${round(float(median),2)}
  Standard Deviation: ${round(standard_deviation,2)}
  Really Cool Boss: {has_cool_owner}
  """

  #Gives a summary of the company
  intro = (f"Company: {company_name} \nDescription: \
  {company_description}\nOwner: {owner}")

  #Gives a summary of the company's accounts
  moneys = (f"Yearly Income: ${yearly_income}\nYearly Expenses:\
  ${yearly_expenses} \nYearly Profit: ${yearly_profit}")

  #compiles accounts into single variable (probably should have sorted)
  i=0
  for x in accounts:
    account_With_Profit = f"{account_With_Profit}{str(accounts[i])}\
    (${str(account_profits[i])})\n"
    i+=1

  #prints all the info 
  #(dont love the indenting, but this was how I had to do it to justify left)
  byline: str = f"""
{intro}\n\n
{moneys}\n\n
{stats_string}\n\n
Accounts: \n{account_With_Profit}
  """
  return byline

def main():
  byline()

#Calls main & runs application if called directly
if __name__ == '__main__':
  main()
