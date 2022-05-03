# Author: Chevaun Duncan
# Date Created: 2/5/2022
# Course:ITT103
# Purpose: To calculate and output the commission earned by a salesperson

def calculator(rate, sales_Amt,):
    rateasP = "{:.2f}".format(rate*100)
    commission = "{:.2f}".format(rate * sales_Amt)
    print("Commission rate is ",rateasP,"%")
    print("Total commission is $",commission)
choice = "y"    
while choice == "y" :
    salesperNum = int(input("Enter the Salespersons number: "))
    sales_Amt = float(input("Enter the Salespersons total amount of sales made $: "))
    sales_Class = int(input("Enter the Salespersons Class: ")) 
    if sales_Class == 1 and sales_Amt <= 1000:  
        rate = 6/100
        calculator(rate, sales_Amt)
        choice = str(input("Would you like to do another salesperson commission? Enter y for yes or e to exit "))
    elif sales_Class == 1 and 1000 < sales_Amt < 2000:  
        rate = 7/100
        calculator(rate, sales_Amt)  
        choice = str(input("Would you like to do another salesperson commission? Enter y for yes or e to exit "))
    elif sales_Class == 1 and sales_Amt >= 2000:  
        rate = 10/100
        calculator(rate, sales_Amt)
        choice = str(input("Would you like to do another salesperson commission? Enter y for yes or e to exit "))
    elif sales_Class == 2 and sales_Amt < 1000:  
        rate = 4/100
        calculator(rate, sales_Amt)
        choice = str(input("Would you like to do another salesperson commission? Enter y for yes or e to exit "))
    elif sales_Class == 2 and sales_Amt >= 1000:  
        rate = 6/100
        calculator(rate, sales_Amt)
        choice = str(input("Would you like to do another salesperson commission? Enter y for yes or e to exit "))
    elif (sales_Class == 3):  
       rate = 4.5/100
       calculator(rate, sales_Amt)  
       choice = str(input("Would you like to do another salesperson commission? Enter y for yes or e to exit "))
    else:  
       print("Please enter valid class!")  
    if choice == "e":
        print("You have exited this program. Have a nice day")
        break
    
   
   
