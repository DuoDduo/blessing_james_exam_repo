# Question 1: Calculator

# function to add two numbers
def add(a,b):
    return a + b

# function to subtract two numbers
def subtract(a,b):
    return a - b

# function to multiply two numbers
def multiply(a,b):
    return a * b

# function to divide two numbers
def divide(a,b):
   try:
        if b== 0 or a==0:
            print("Error: input cannot be a negative number")
        else:    
            return a / b
   except ZeroDivisionError as e:
         print("Error: ", e)
    

# Main program
def main():
    while True:
        try:
           #Calculator menu
            print("\nWelcome to Blessing's Calculator")
            print("1. Add (+)")
            print("2. Subtract (-)")
            print("3. Multiply (*)")
            print("4. Divide (/)")
            print("5. Exit")

           #collect input from user 
            choice = int(input("Enter between (1-5) to select your desired calculator operation: "))
            # Validate choice using range
            if choice not in range(1, 6):
                print("Invalid choice! Please choose a number between 1 and 5.")
                continue
            if choice == 5:
                print("Exiting calculator...")
                break  

            # Handle user inputs for each operation
            if choice in range(1,6):
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                    # Display calculator menu
                if choice == 1:
                    result = add(a, b)
                elif choice == 2:
                    result = subtract(a, b)
                elif choice == 3:
                    result = multiply(a, b)
                elif choice == 4:
                    result = divide(a, b)
               # Exit condition
            

            print(f"Result =  {result}")
            
            # Ask if user wants to perform another calculation and strip removes unnecessary spaces, lower ensure input is validated as alower
            again = input("Do you want to perform another operation? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Thanks for using the calculator. Goodbye!")
                break
        # this catches the errors in the programme
        except ValueError:
            print("Error: Please enter a valid number!")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Run the calculator
if __name__ == "__main__":
    main()    







# Question2
while True:# A loop that runs until user type exit
    # collects input from user
    user_input = input("\nEnter a number (or type 'exit' to quit): ")

    if user_input == "exit":
        print("Goodbye!\n")
        break  # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even") #check fif a number is odd
    else:
        print("The number is odd") #check if a number is even






#  Question 3 
while True:
    try: # handling errors
        # collecting age input from user
        age = input("\nEnter your age (or type exit to quit): ")
        # control flow
        if age == "exit":
            print("\nGoodbye!")
            break
        # age validation
        elif int(age) >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
            # display error message
    except ValueError:
        print("Invalid input, Please enter a number")