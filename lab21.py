def displayWelcome():
    print('to calculate loan payoff for the issued loan amout for a credit card');
def displayPayments(balance,int_rate,monthly_payment):
    num_months=0;
    total_int_paid=0;
    payment_num=1;
    balance1=balance;
    empty_year_field=format(' ','8');

    print('\n', format('LOAN PAYOFF SCHEDULE','20'));
    print(format('year','>10')+format('balance','>10')+format('payment num','>18')+format('Monthly iterest paid','>20')+format('Total interest paid','>20'));
    while balance>0:
        monthly_int=balance*int_rate;
        total_int_paid=total_int_paid+monthly_int;

        balance=(balance+monthly_int)-monthly_payment;

        if balance<=0:
            balance=0;
        if num_months%12 ==0:
            year_field=format(num_months//12+1, '>8');
            
        else:
            year_field=empty_year_field
        print(year_field+format(balance,'>12.2f')+format(payment_num,'>9')+format(monthly_int,'>18.2f')+format(total_int_paid,'>18.2f'));
        payment_num=payment_num+1;
        num_months=num_months+1;
    print("\n");
    print("Total interest paid to pay off is", round(total_int_paid));
    print("\n");
    print("Total amount(Loan maount+interest) paid to pay off is", round(total_int_paid+balance1));
         
        

# main
displayWelcome();
balance=int(input('enter loan amopunt  on creit card'));
apr=int(input('enter annual percentage of interest'));
monthly_int_rate=apr/1200;
response=input(' will you use minimum payment(y/n)');
if response in ('y','Y') and balance<=100000:
                min_monthly_payment=5000;
else:
                min_monthly_payment=balance*0.05;
if response in ('n','N'):
    amount=int(input('Enter amount'));
    while amount<balance*0.05:
        amount=int(input('Re-Enter amount'));
    min_monthly_payment=amount;
           
displayPayments(balance,monthly_int_rate,min_monthly_payment);

    
        
                              
            
        
          
        
