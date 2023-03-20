import math
print("Welcome to Finance Calculator \n") # Welcome Message for the user to ensure they know they are using a finance calc.
# print option statments so that the user is aware of the options availble in this program
print("investment - to calculate the amount of interest you'll earn on your investments \nbond       - to calculate the amount you'll have to pay on a home loan\n")
options = str(input("either enter 'investment' or 'bond' from the menu above to proceed \n> ")) # give user options from the menu to select to continue
# create if/else statments for investment part of the menue
if options.lower() == "investment":# if variable options in any case equals the input "investments" it will display below 
    if True: 
        deposit = float(input("Enter deposit amount: ")) # asks user to enter deinposit amount. use float due to not knowing where the input maybe whole or dec
        interest = float(input("Enter your interest rate - eg. 5 : ")) # asks user to input interest amount. use float due to not knowing where the input maybe whole or dec
        years = float(input("Enter number of years investing: ")) # asks user to input number of years.use float due to not knowing where the input maybe whole or dec
        interest_choice = str(input("Choose between simple or compounding interest below \n> ")) # with the varible interest, ask the user to choose between simple or compound calc.
     
        if interest_choice.lower() == "simple": # condition for simple interest with print statement and calculation of outcome
         print("deposit = ", deposit ,"\ninterest =", interest , "\nyears = ", years ,  "\nThe total amount when simple interest is applied is calcuated at " , deposit*(1+(interest/100)*years),"pounds")   
        elif interest_choice.lower() == "compounding": # conditon for compound interest with print statement and calculation of outcome.
         print("deposit = ", deposit ,"\ninterest =", interest , "\nyears = ", years ,"\nThe total amount when compoudning interest is applied is calcuated at" ,deposit * math.pow((1 + (interest/100)),years), "pounds")

#conditional statement if bond was inputted by user
elif options.lower() == "bond": #if statment for bond with inputs for the data required for the calculation
    if True:
     house_value = float(input("enter house value amount: "))
     interest_one = float(input("Enter your interest rate - eg. 5 : "))
    months = float(input("Enter number of months you plan it will take to pay back bond: "))
    print("House value: ", house_value , "\nInterest: ", interest_one , "\nMonths: ", months , "\nThe total amount you will have to pay each month is calcuated at", ((interest_one/100)*house_value) / (1+(interest_one/100))**(-months), "pounds")
#if any input by the user is incorrect they will be shown this message.
else: 
    print("Incorrect data entered, please try again.")
 



    

