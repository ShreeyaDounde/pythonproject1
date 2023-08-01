# #a simple list
# list=[1,2,3,4,5,'Abhi'];
# #print the list
# print(list);
# #print type of list
# print(type(list));

#repetation of the list
# list1=['Abhi','IT',50000]
# i=list1*2
# print(i);

#concatanation of lists

# list1=[1,2,3,4,5,6];
# list2=[7,8,9,10];
#
# i=list1+list2;
# print(i);

#calculate the length of list

# list=[1,1,2,3,4,5];
# print(len(list));

#iteration of list

# list=[1,2,3,4,5];
# for i in list:
#     print(i);
#
#membership of list

# list=[100,200,300,400];
#
# print(100 in list);
# print(700 in list);
# print(200 in list);
# print(900 in list);

# a=[1,2,'Ram',3.50,100];
# b=[1,2,'Ram',3.40,100];
# print(a==b);

#list slicing
# emplist=[101,'Soniya',50000,'IT'];
# print(emplist);
# print(emplist[0]);
# print(emplist[1]);
# print(emplist[2]);
# print(emplist[3]);
#
# list=[1,2,3,4,5];
# print(list[:]);
# print(list[0:]);
# print(list[2:]);
# print(list[4:]);
# print(list[1]);
# print(list[:3]);
# negative index
# print(list[-1]);
# print(list[:-3]);
# print(list[:-4]);
#
##Display list
# lst=[200,300,4000,500];
# print(lst);
# print(lst[-3:2]);
# print(lst[-2::-1]);
# print(lst[-1:-3]);
# print(lst[-4:3]);
# print(lst[4::-1]);
# emplist=[101,'Yusuf',90000,'IT'];
# print(emplist);
# emplist[2]=1900000;
# emplist[1]='Ravan'
# print(emplist);
# emplist[-1]='Civil';
# emplist[-3:-2]=['Sonali',200000];
# print(emplist);

# thislist=['banana','Apple','kiwi','mango'];
# print(thislist);
# thislist[1:3]=['watermelon','berry'];
# print(thislist);
# thislist[1:2]=['blackcurrent','cherry'];
# print(thislist);

#list methods

# list1=['lion','tiger','mouse',];
# print(list1);
# list1.append('Elephant');
# print(list1)
# wildanimal=['Wolf','fox'];
# list1.append(wildanimal);
# print(list1);

#clearing the list
# list1=['apple','banana','custurdapple','grapes'];
# list2=['orange','kiwi','dragonfriut','berry'];
# print(list1);
# print(list2);
# list1.clear();
# print(list1);
# del list2[:];
# print(list2)

#copying the list

# my_list1=[1,2,'cat'];
# print(my_list1)
# newlist=my_list1.copy();
# print(newlist)
#
# old_list=[1,2,3];
# print(old_list)
# newlist=old_list;
# print(newlist);
# newlist.append(4);
# print(newlist)

#count method
# list1=[1,2,3,2,4,5,2];
# print(list1)
# print(list1.count(2));
#
# vowels=['a,''e','i','i','o','u'];
# print(vowels);
# print(vowels.count('i'))

##extend method
# evennumbers=[2,4,5];
# print('even nu:',evennumbers)
# oddnumbers=[3,5,7];
# print('odd numbers',oddnumbers);
# #exentended list
# evennumbers.extend([102,200]);
# print('updated list',evennumbers);

# languge_list=['french'];
# print(languge_list);
# lang_tuple=('englsh','chinese');
# languge_list.extend(lang_tuple);
# print(languge_list);
# lang_set={'Japnese','Hindi'};
# languge_list.extend(lang_set);
# print(languge_list)
#
# a1=[1,2,3];
# a2=[1,2,3];
# b=(4,5);
# a1.extend(b);
# print(a1)
# a2.append(b);
# print(a2)
# print(len(a2));
#
# print(a2.index(1));
# print(languge_list.index('Hindi'));
# indexofhindi=languge_list.index('Hindi',4);
# print(indexofhindi)

# fruits=['apple','banana','mango'];
# fruits[1]=['orange'];
# print("updated list",fruits);
# fruits.insert(1,'Cherry');
# print(fruits)

#sort method
numbers=[2,4,6,8,10];
print(numbers);
numbers.sort(reverse=True);
print(numbers)

