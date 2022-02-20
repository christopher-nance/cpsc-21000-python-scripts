# Christopher Nance
# Version 1.0
# 2/4/2022
# CPSC 210000 Homework #3
# Prof. Klump

# The purpose of this program is to calculate the mortgage payment for someone given the following user input: i rate, cost of the house, down payment and loan term. 
# A $100 insurance fee is assessed if the downpayment is < 20% of the cost of the home.

print(r'''
******************************************************************
              HOME MORTGAGE PAYMENT CALCULATOR V1.0
******************************************************************
In this program, we will calculate your monthly mortgage payment.
You will enter the cost of the home you are buying and how much
of a down payment you are making. You will then enter the annual
interest rate as well as the length of the loan in years. The 
The program will take this information and compute your monthly
mortgage payment. If your down payment is less than 20% of the
cost of the home, you will have to pay a mortgage insurance fee
of $100 per month.
''')



### USER INPUT | VARIABLES ###
cost_of_home = float(input("Enter the cost of the home you want to buy: "))
down_payment = float(input("Enter the amount of money you wish to put down: "))
interest_rate = float(input("Enter the interest rate (annual %): "))
loan_duration = int(input("Enter the amount of years you will have this loan: "))



### CALCULATED OUTPUTS | VARIABLES ###
PV = cost_of_home - down_payment
i = (interest_rate/100)/12
n = loan_duration*12
PMT = i*PV/(1-(1+i)**-n)
insurance = 0.00
if down_payment/cost_of_home < 0.20: insurance = 100.00
total_per_month = PMT+insurance



### TABLE TO FORMAT FOR OUTPUT ###
loan_summary = [
    ["Loan Amount", "$", ("%.2f" % PV)],
    ["Interest Rate", "", ("%.2f" % interest_rate)+"%"],
    ["Number of Years", "", loan_duration],
    ["Monthly Mortgage", "$", ("%.2f" % PMT)],
    ["Mortgage Insurance", "$", insurance],
    ["Total Cost per Month", "$", ("%.2f" % total_per_month)],
]

print("\nHere is a summary of your loan:")
for item in loan_summary: print("{: <20} {: >20} {: >20}".format(*item)) # https://docs.python.org/2.7/library/string.html#format-specification-mini-language



print('''
******************************************************************
                Thank you for using this program.
******************************************************************
''')