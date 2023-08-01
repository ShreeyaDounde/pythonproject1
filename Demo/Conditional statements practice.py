# kitchen="Apple"
# if(kitchen=='Apple'):
#     print('yes there is an apple');
# print('there is no apple');
# if(kitchen=='mango'):
#     print('yes here it is');
# print('no not here is an apple')

#num=20;
# if(num<15):
#     print('number is smaller than 15');
# print('number is not smaller than 15')#this statement is always print either if condition is true or false
#

# if('Python'in['Java','Python','C']):
#     print(True)

#if else statement

# a=1;
# b=2;
# if(a==b):
#     print('True');
# else:
#     print('False');
# print('Relax');

# management_list=['Amit','Pooja','Sanika'];
# management_tuple=('Priya','Parag','Patil');
# if("Amit" in management_list):
#     print('he is part of management_list');
# if("Amit" not in management_list):
#     print('he is not in list');
# if("Amit"in management_tuple):
#     print('he is in tuple');
# if("Amit"not in management_tuple):
#     print('he is not in tuple');
# print('relax');
# passing_score=float(input('enter the score'));
# my_score=float(input('enter the my_score'));
# if(my_score>=passing_score):
#     print("congratulation !u passed the exam");
# else:
#     print('u failed in exam');

# num=5;
# if(num==0):
#     print('num is zero');
# elif(num>5):
#     print('number is greater than 5');
# elif(num<5):
#     print('num is less than 5');
# else:
#     print("number is smaller than 5");
#

# num=-7;
# if(num!=0):
#     if(num>0):
#         print('number is positive');
#     else:
#         print('number is negative');
# else:
#     print('number is zero');

#
#leap year programm
current_year=int(input('enter the year'));
month=int(input('enter the month number'));
if((current_year%4)==0):
    print('Leap year');
    if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        print("there are 31 days in month");
    elif(month==4 or month==6 or month==9 or month==11):
        print("months having 30 days");
    elif(month==2):
        print("month having 29 days");
    else:
      print("Invalid month");
else:
    print("Invalid year");