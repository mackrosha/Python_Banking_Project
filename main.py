import sys
import json  # Use json to easily serialize and deserialize account data
accounts = {}
# Load accounts from file if it exists
def load_accounts():
    try:
        with open('accounts.txt', 'r') as f:
            global accounts
            accounts = json.load(f)
            print("Accounts loaded successfully!\n")
    except FileNotFoundError:
        print("No account data found, starting fresh!\n")
# Save accounts to file
def save_accounts():
    with open('accounts.txt', 'w') as f:
        json.dump(accounts, f)
    print("Accounts saved successfully!\n")
# Function to create a new account
def create_account():
    account_number = input("Enter a New Account Number (integer number only): ")

    if account_number in accounts:
        print("Account number already exists!")
        return

    name = input("Enter your Account Name: ")
    initial_deposit = float(input("Enter the initial deposit for New Account: "))

    accounts[account_number] = {'name': name, 'balance': initial_deposit}
    print(f"Account created successfully for {name} with Account Number {account_number}.\n")

    save_accounts()  # Save the account data after creating the account


def check_account_details():
    account_number = input("Enter your Account Number: ")

    if account_number not in accounts:
        print("Account not found!")
        return

    account_info = accounts[account_number]
    print(f"Account Number: {account_number}")
    print(f"Account Holder Name: {account_info['name']}")
    print(f"Account Balance: {account_info['balance']}\n")



# Function for deposit
def deposit():
    account_number = input("Enter your Account Number: ")

    if account_number not in accounts:
        print("Account Number Not Found")
        return

    amount = float(input("Enter Amount To Deposit: "))
    accounts[account_number]['balance'] += amount
    print(f"Deposit successful! New balance: {accounts[account_number]['balance']}\n")

    save_accounts()  # Save the account data after deposit


# Function for withdrawal
def withdraw():
    account_number = input("Enter your Account Number: ")

    if account_number not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter amount to withdraw: "))

    if amount > accounts[account_number]['balance']:
        print("Insufficient balance!")
        return

    accounts[account_number]['balance'] -= amount
    print(f"Withdrawal successful! Remaining balance: {accounts[account_number]['balance']}\n")

    save_accounts()  # Save the account data after withdrawal


# Function to check account balance
def show_balance():
    account_number = input("Enter your Account Number: ")

    if account_number not in accounts:
        print("Account not found!")
        return

    print(f"Account balance: {accounts[account_number]['balance']}\n")


# Menu for CLI
def menu():
    load_accounts()  # Load accounts data at the start

    while True:
        print("++++++++Banking System+++++++++")
        print("1. Create a New Account")
        print("2. Check Account Detials")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Balance Check")
        print("6. Exit")
        choice = int(input("Enter your Choice (1-5): "))

        if choice == 1:
            create_account()
        elif choice == 2:
            check_account_details()
        elif choice == 3:
            deposit()
        elif choice == 4:
            withdraw()
        elif choice == 5:
            show_balance()
        elif choice == 6:
            print("Thank you for using our banking system!")
            sys.exit()
        else:
            print("Invalid choice! Please choose again.\n")


if __name__ == "__main__":
    menu()
