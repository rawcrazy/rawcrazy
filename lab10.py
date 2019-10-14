import math;
terminate=False;
print('pgam to display DAY OF THE WEEK');
while not terminate:
    month=int(input('enter the month'))
    if month==-1:
            terminate=True;
    else:
            while month<1 or month>12:
                  month=int(input('invalid month, re-enter month between 1 and 12'));
            year=int(input('enteryear'));
            day1=int(input('enter day'));
            while year < 1800 or year>2099:
                       year=int(input('invalid year- re-enter year'));
            if(year%4==0) and (not(year%100==0) or (year%400==0)):
                            leap_year=True;
            else:
                            leap_year=False;
            if month in (1,3,5,7,8,10,12):
                        num_days_in_month=31;
            elif month in(4,6,9,11):
                        num_days_in_month=30;
            elif leap_year:
                        num_days_in_month=29
            else:
                        num_days_in_month=28;
# To determine thedayof week
            century_digits=year//100;
            year_digits=year%100;
            
            value=year_digits+math.floor(year_digits/4);
            
            if century_digits==18:
                    value=value+2;
            elif century_digits==20:
                    value=value+6;
                    
            if month==1 and not leap_year:
                    value=value+1;
            elif month==2:
                    if leap_year:
                            value=value+3;
                    else:
                            value=value+4;
            elif month==3 or month==11:
                            value=value+4;
            elif month==5:
                            value=value+2;
            elif month==6:
                            value=value+5;
            elif month==8:
                            value=value+3;
            elif month==9 or month==12:
                            value=value+6;
            elif month==10:
                            value=value+1;

            day_of_week=(value+day1)%7    # 1-sunday, 2-monday,.....
           
           # print('dayof theweek is',day_of_week);

            if month==1:
                month_name='January'
            elif month==2:
                 month_name='February'
            elif month==3:
                 month_name='March'
            elif month==4:
                 month_name='April'
            elif month==5:
                 month_name='may'
            elif month==6:
                 month_name='June'
            elif month==7:
                 month_name='July'                
            elif month==8:
                month_name='August'
            elif month==9:
                 month_name='september'
            elif month==10:
                 month_name='October'
            elif month==11:
                 month_name='November'
            else:
                 month_name='December'
            if leap_year:
                            print('\n',' ',month_name,year,'(Leap Year)','HAS',num_days_in_month,'DAYS' );
            else:
                            print('\n',' ',month_name,year,'HAS',num_days_in_month,'DAYS' );
            if day_of_week==1:
                print('SUNDAY');
            elif day_of_week==2:
                 print('MONDAY');
            elif day_of_week==3:
                 print('TUESDAY');
            elif day_of_week==4:
                 print('WEDNESDAY');
            elif day_of_week==5:
                 print('THURSDAY');
            elif day_of_week==6:
                 print('FRIDAY');
            elif day_of_week==0:
                 print('SATURDAY');
                
