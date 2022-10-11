#this program will allow users to keep track of their expenditures against an overall budget of 2500. The expenses will be entered and compared against the allocated budget. A summary is then displayed to get a quick overview of the finances. 
#initially, this program will only allow the user to add 3 budgeting items

#functions are added sequentially to create the budget library. Next, a summary of all of the expenses is printed. In the end, all the code is converted to a python class. 

budgets= {}
expenditures= {}

print("Welcome to the budget manager program! We will help you keep track of your savings")

budget_available= input("Please enter what your total budget is: ")
budget_available= int(budget_available)

def add_budget(name, int(amount)):
    global budget_available
    if name in budgets:
    
        raise ValueError("Budget Exists!")
    if int(amount) > budget_available:
        raise ValueError("Insufficient funds")
    budgets[name]= int(amount) 
    budget_available-= int(amount) 
    expenditures[name] =0
    return budget_available

def spend(name, amount):
        #a function to track the expenditures. Do this by adding a function that allows you to enter the money that has been spent and then add another function to display the summary. Summary will indicate the total money spent and the amount remaining
        if name not in expenditures:
            raise ValueError("No such budget")
        expenditures[name] += amount 

        budgeted = budgets[name]
        spent= expenditures [name]
        remaining= budgeted-spent
        return remaining 

def print_summary():

    #a function that will display an overview of each budget name, the amount originally budgeted, the amount spent and whats left to spend. also adding some formatting so that the information is presented in a table format 
    print("Budget           Budgeted    Spent   Remaining")
    print('---------------  ----------  ------  ---------')

    total_budgeted = 0
    total_spent=0
    total_remaining = 0

    for name in budgets:
        budgeted= budgets[name]
        spent= expenditures[name]
        remaining = budgeted - spent 
        print(f'{name:15s} {budgeted:10.2f} {spent:10.2f} {remaining:10.2f}')
    total_budgeted += budgeted
    total_spent +=spent
    total_remaining += remaining

    #table footer: 
    print('---------------  ----------  ------  ---------')
    print(f'{"Total":15s} {total_budgeted:10.2f} {total_spent:10.2f} {total_budgeted - total_spent:10.2f}')





print("Please list the name of the item and amount you are trying to budget below:")

budget1= input ("First budget item:")
amount1= input("Amount: ")

firstRun: add_budget(budget1, amount1)
print("Your remaining budget is"+ str(firstRun))
amount1= int(amount1) 


budget2= input("Second budget item:")
amount2= input("Amount:")
amount2= int(amount2) 


secondRun= add_budget(budget2, amount2)
print("Your remaining budget is now" + str(secondRun))

budget3= input("Third budget amount")
amount3= input("Amount:")
amount3= int(amount3) 


thirdRun= add_budget(budget3, amount3)
print("Your remaining budget is"+ str(thirdRun))

budgets= {budget1, budget2, budget3}
expenditures= {amount1, amount2,amount3}

print("Now we will print out a summary for you that includes all the budgets and expenditures")

print_summary()














