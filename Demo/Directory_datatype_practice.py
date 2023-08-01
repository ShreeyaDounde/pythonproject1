#create directory
# D={'name':'Bob','job':'Tester','salary':40000,'age':25,'email':'bobthe@gmail.com'};
# print(D)
# # create directory using dict()constructor
#
# d1=dict({1:'Geeks',2:'for',3:'Geeks'});
# print(d1)

#create directory with of list of 2 items tuple
# L=[('name','Bob'),('age',20),('job','IT')];
# D=dict(L);
# print(D)
# print(type(D))
#
# E=[(1,2),(20,30)]
# C=dict(E);
# print(C)
# print(type(C))

#create directory with tuple
# D=dict(name='Bob',surname='the_Builder');
# print(D)

#create directory with zipped keys and values

keys=['name','age','city'];
values=['Bob',25,'Pune']
D=dict(zip(keys,values));
print(D)
#output={'name': 'Bob', 'age': 25, 'city': 'Pune'}

#create a dictionary with default values for each key. The fromkeys() method
# keys=['a','b','c'];
# deaultvalues=0;
# D=dict.fromkeys(keys,deaultvalues);
# print(D)

# keys=[1,2,3,4,5];
# defaultvalues='digits';
# d=dict.fromkeys(keys,defaultvalues);
# print(d);

# keys=['a','e','i','o','u'];
# defaultvalues='Vowels';
# d=dict.fromkeys(keys,defaultvalues)
# print(d)

#keys are must be unique it can not accept duplicate keys

# D={'name':'Bob','age':30,'name':'Angle'}
# print(D)

#keys must be immutable(an exception can be raised when mutable object is used as key)

# D={(2,2):25,
#    True:'a',
#    'name':'Bob'};
# print(D)

# D={[2,2]:30,'name':'Bob'}
# print(D)
#the error shown isTypeError: unhashable type: 'list'

#values can be any type

# D={1:[1,2,3],
#    2:[0,1]}
# print(D)

#duplicate values

# D={1:[1,2],2:[1,2],3:[1,2]}
# print(D)

#Access directory items
# A={'name':'Bob','age':25,'dept':'IT'}
# print(A['name'])
# print(A['age'])
# print(A['dept'])
# #print(A['salary'])#it shows key error
# print(A.get('name'))
# print(A.get('salary'))#it prints none for keys which are not present in the directory

#create nested directories
# dir={'dir1':{1,2},'dir2':{3,4}};
# print(dir['dir1']);#accesing the nested directory
# print(dir['dir2'])

#Add or update directory items
# D={'name':'Bob','age':28};
# print(D)
# D['name']='sam';
# print(D)
# D['age']=30
# print(D)
# #adding the new key and value
# D['city']='Pune'
# print(D)