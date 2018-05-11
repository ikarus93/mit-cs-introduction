'''Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance.
At the end of 12 months, print out the remaining balance. 
Be sure to print out no more than two decimal digits of accuracy'''

def getBalance(balance, annualInterestRate, monthlyPaymentRate, month):
  monthlyInterest = annualInterestRate / 12
  minimumMonthlyPayment = monthlyPaymentRate * balance
  unpaidBalance = balance - minimumMonthlyPayment
  balance = round(unpaidBalance + (monthlyInterest * unpaidBalance), 2)
  if month == 11:
    return balance
  else:
    month += 1
    return getBalance(balance, annualInterestRate, monthlyPaymentRate, month)

print("Remaining Balance: " + str(getBalance(balance, annualInterestRate, monthlyPaymentRate, 0)))