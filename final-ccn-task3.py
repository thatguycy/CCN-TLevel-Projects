#######################################################################################
#### CCN Digital Production, Design & Development Level 3 College Interview Task 3 ####
#### by Harvey Washington (hjw45h@gmail.com)                                       ####
#### Python 3.9                                                                    ####
#######################################################################################

ans = None # Define ans as a fallback to prevent undefined later on.

def calc(choice):
    num1 = float(input("[1] Enter the first number: ")) # Define num1 by user input as a float to allow for decimals.
    num2 = float(input("[2] Enter the second number: ")) # Define num2 by user input as a float to allow for decimals.
    opr = f'{num1}{choice}{num2}' # Define the operation that needs to be run.
    try:
        exec(f'ans = {opr}', globals()) # Store the answer for the operation as the variable 'ans'.
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        mainMenu()
    print(f'\n[A] The Answer is: {ans}') # Print the answer.

def mainMenu():
    print("[+] Addition\n[-] Subtraction\n[*] Multiplication\n[/] Division\n") # Display 4 options on 4 different lines.
    choice = input("[?] Enter your choice: ") # Accept the User's Input
    if choice == "+" or choice == "-" or choice == "*" or choice == "/": # Make sure they're using a valid option from the menu.
        calc(choice) # Call the calculation function
    else:
        print(f'[!] Invalid Input Type "{choice}"') # Warn the user they've selected an invalid function
        mainMenu() # Redirect them to the main menu again.

mainMenu()
