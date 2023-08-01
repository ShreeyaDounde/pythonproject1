#create tuple
# mytuple=(1,2,3,4);
# print(mytuple);
# #tuple with mixed datatypes
# tuple=(1,2,'hello',8.9);
# print(tuple);
# #nested tuple
# tuple1=(1,2,9,(23,20),(60,99));
# print(tuple1);
# #tuple datatype
# var1=("hello");
# print(var1)
# print(type(var1));
# #creating tuple with one element
# var2=("hello",);
# print(type(var2));

#tuples can be joind by using concatanation & replication operator

# tuple=(1,2,3,4)+(100,200,300);
# print(tuple);
# t=('a','e','o')+(1,2,3);
# print(t);
# tuple2=tuple+t;
# print(tuple2)
#
# #replication or repetation
# t1=('red',)*3;
# print(t1);
#
# #membership
#
# t2=('red','green','blue');
# print('red'in t2);
#
# #iteration
# t3=1,2,3,4;
# print(t3);
# for i in t3:
#     print(i);
# #length of tuple
# print('length of t3',len(t3));
#
# colors=('red','green','blue','white');
# print(colors);
# print(colors.index('red'));
# print(colors[1])
# print(colors[3]);
# #print(colors.append('black'))
# print(colors[-1]);
# print(colors[1:]);
# print(colors[::-1])
# print(colors[-3:-1])
# print(colors[:])
# print(colors[0:4:2])

#packing and unpacking
# t=(1,2,3,4,5);
# (a,b,c,d,e)=t;
# print(a);
# print(b)
# print(c)
#converting list into tuple
# a=[1,2,3,4,5,6]
# print(a)
# b_tuple=tuple(a);
# print(type(b_tuple));

#tuple methods

# a=(1,2,3,4,5,1,5,9);
# print(a.index(5));
# print(a.count((1)));
#
# tuple2=(100,300,700,899,200);
# print(min(tuple2));
# print('print max value of tuple:',max(tuple2));
# print("print sum of tuple:",sum(tuple2));
# tuple1=('hello','hi','good','morning');
# print(tuple1)
# print("max value of tuple:",max(tuple1));
# sorted_=tuple(sorted(tuple2));
# print('sorted tuple:',sorted_);
# print(type(sorted_))
# sorted_=tuple(sorted(tuple2,reverse=True));
# print(sorted_)

# p=(900,700,200,500,600);
# sort=tuple(sorted(p,reverse=True));
# print(sort);
# sort=tuple(sorted(p));
# print(sort)

#type casting
# p=[1,2,3,4]
# print(p);
# tuple_A=tuple(p);
# print(tuple_A);
# print(type(tuple_A));
# a_list=['a','a','b'];
# tuple_b=tuple(a_list);
# print(tuple_b);
# print(type(tuple_b))
#converting string into tuple
# a='Sonia'
# print(type(a))
# tuple_A=tuple(a);
# print(tuple_A);
#print(type(tuple_A))

#converting tuple into list
# a=(1,2,3)
# print(a)
# list_a=list(a);
# print(type(list_a))
# print(list_a)


