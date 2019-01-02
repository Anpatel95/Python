
def subdirect(pri, y, t):
    i = 0.034 #static interest rate
    f = 0.01051 #static fee rates
    
    m = (pri * i)/(t * (1-(1+i/t)**(-y*t))) #monthly payments
    balance = (m * t * y) #total paid on loan
    intPaid = (balance - pri) #interest paid
    fee = (pri * f) #fees paid
    totalCPri = intPaid + fee #total costs over principle
    
    #output of subsidized loan
    print("------------------------------")
    print("Subsidized Federal Direct Loan")
    print("Principle:", pri)
    print("Interest Rate:", 3.4)
    print("Years:", y)
    print("Monthly Payment", round(m,2) )
    print("Total Paid on Loan:", round(balance,2))
    print("Total Interest Paid:", round(intPaid,2))
    print("Additional Fees Paid:", round(fee,2))
    print("Total Costs Over Principle:", round(totalCPri,2))
    
def unsubdirect(pri, y, t):
    i = 0.068#static interest rates
    f = 0.01051 #static fee rates
    new_pri = pri *(1+i*4.25) #new Principle value
    
    m = (new_pri * i)/(t * (1-(1+i/t)**(-y*t))) #monthly payments
    balance = (m * t * y) #total paid on loan
    intPaid = (balance - pri) # total interest paid
    fee = (pri * f) #fees paid
    totalCPri = intPaid + fee #total costs over principle
    
    #output of unsubsidized loan
    print("------------------------------")
    print("Unsubsidized Federal Direct Loan")
    print("Principle:", pri)
    print("Interest Rate:", 6.8)
    print("Years:", y)
    print("Monthly Payment", round(m,2) )
    print("Total Paid on Loan:", round(balance,2))
    print("Total Interest Paid:", round(intPaid,2))
    print("Additional Fees Paid:", round(fee,2))
    print("Total Costs Over Principle:", round(totalCPri,2))
    
def fedplus(pri, y, t):
    i = 0.079#static interest rate
    f = 0.04204#static fee rates
    
    new_pri = pri *(1+i*4.25) #new principle value
    
    m = (new_pri * i)/(t * (1-(1+i/t)**(-y*t))) #monthly rate
    balance = (m * t * y) #total paid on loan
    intPaid = (balance - pri) #total interest paid
    fee = (pri * f) #fees paid
    totalCPri = intPaid + fee #total costs over principle
    
    #output of federal plus loan
    print("------------------------------")
    print("Federal Plus Loan")
    print("Principle:", pri)
    print("Interest Rate:", 7.9)
    print("Years:", y)
    print("Monthly Payment", round(m,2) )
    print("Total Paid on Loan:", round(balance,2))
    print("Total Interest Paid:", round(intPaid,2))
    print("Additional Fees Paid:", round(fee,2))
    print("Total Costs Over Principle:", round(totalCPri,2))





if __name__ == "__main__":
    print("Welcome to the Student Loan Calculator")
    pri = int(input("Enter the amount of the loan in dollars with (no commas):\n"))#user input loan amount
    y = int(input("Enter the number of years the loan will be for:\n")) #user input years
    t = 12 #static 12 months time
    subdirect(pri, y, t)
    unsubdirect(pri, y, t)
    fedplus(pri, y, t)
    
    
    
