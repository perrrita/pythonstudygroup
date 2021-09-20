principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = int(input("which month are you starting your extra payments? ")) #get input from user and turn the string into integer
extra_payment_end_month = int(input("which month are you ending your extra payments? "))
extra_payment = int(input("how many dollars are you paying? $"))
month = 0

while principal > payment: #if principal < payment, we won't do this loop so we won't overpay in the last month
    month = month + 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        this_month_payment = payment + extra_payment
    else:
        this_month_payment = payment
    principal = principal * (1+rate/12) - this_month_payment #this is outside of if statement so will happen regardless
    total_paid = total_paid + this_month_payment
    
    print(month, round(total_paid,2), round(principal,2)) #print the table

month = month + 1 #need to write this again as we're not in the loop
payment = principal * (1+rate/12) #set the final payment to be the principal plus final month's interest
total_paid = total_paid + payment
principal = principal * (1+rate/12) - payment #this will bring it to 0

print(month, round(total_paid,2), round(principal,2))
print("total paid", round(total_paid, 2))

