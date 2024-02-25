from expense import Expense

def main():
    print(f"Running expense file ")
    
    #get user to input their text 
    expense=get_user_expense()
    print(expense)
    # write their expense to file 
    save_expense_to_file

    # read the file and summrasize all the expenses 
    summarize()

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

def save_expense_to_file():
    print(f"Save user expense:")

def summarize():
    print(f"Summarize user expense:")

if __name__=="__main__":
    main()