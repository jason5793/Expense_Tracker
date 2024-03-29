from expense import Expense
from typing import List

def main():
    print(f"Running expense file ")

    expense_file_path="expenses.csv"
    
    #get user to input their text 
    expense=get_user_expense()
    # write their expense to file 
    save_expense_to_file(expense,expense_file_path)

    # read the file and summrasize all the expenses 
    summarize(expense_file_path)

def get_user_expense():
    print("Getting user expense:")
    expense_name=input("Enter expense name:")
    expense_amount=float(input("Enter expense amount:"))


    expense_categories=[
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc",
    ]


    while True:
        print("Select a Category: ")
        for i,category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")
        value_range =f"[1-{len(expense_categories)}]"
        select_index=int(input(f"Enter a category number{value_range}:"))-1
        if select_index in range(len(expense_categories)):
            selected_catgegory=expense_categories[select_index]
            new_expense=Expense(
                name=expense_name,category=selected_catgegory,amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid Category. Please try again")



def save_expense_to_file(expense:Expense,expense_file_path):
    print(f"Save user expense:{expense} to{expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")


def summarize(expense_file_path):
    print(f"Summarize user expense:")
    expenses:list[Expense]=[]
    with open(expense_file_path, "r") as f:
        lines=f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_catgory=line.strip().split(",")
            line_expense=Expense(
                name=expense_name,
                amount=expense_amount,
                category=expense_catgory
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key=expense.category
        if key in amount_by_category:
            amount_by_category[key]+=expense.amount
        else:
            amount_by_category[key]=expense.amount
    
    print("Expense by Category:")
    for key, amount in amount_by_category.items():
        print(f"{key}: ₹{amount}")

if __name__=="__main__":
    main()