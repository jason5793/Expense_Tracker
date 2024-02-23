def main():
    print(f"Running expense file ")
    
    #get user to input their text 
    get_user_expense()
    # write their expense to file 
    save_expense_to_file

    # read the file and summrasize all the expenses 
    summarize()

def get_user_expense():
    print("getting user expense:")
    expense_name=input("Enter expense name:")
    expense_amount=float(input("Enter expense name:"))
    print(f"You have entered:{expense_name},{expense_amount}")
def save_expense_to_file():
    print(f"Save user expense:")

def summarize():
    print(f"Summarize user expense:")

if __name__=="__main__":
    main()