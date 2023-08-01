# a="Hello";
# b="world";
# c=a+""+b;
# print(c);
#
# city="Ahmadabad";
# print(city);
# print(type(city));

# a="Python";
# print(a*10);
#
# print("python\n"*10);
# print("Priya\t"*5);

# string1="credence";
# print(string1);
# print(string1[0]);
# print(string1[1]);
# print(string1[2]);
# print(string1[3]);

string='CredenceAutomation';
print(string[0]);
print(string[3]);
print(string[0:3]);
print(string[0:7]);
print(string[2:8]);
print(string[-7:-2]);
print(string[-2:-7]);
print(string[8:18]);
print(string[8:]);
print(string[18:8]);
print(string[3:15]);
print(string[-1]);
print(string[-3:]);
print(string[-3]);
print(string[3:-10]);
print(string[3:-16]);
print(string[3:-11]);
print(string[-3:18]);
print(string[-2:-5]);
print(string[-2:7]);
print(string[2:-7]);
print(string[-5:-2]);
print(string[1:10:2]);
print(string[-1:-12:-2]);
#prints string in reverse format
print(string[::-1]);
print(string[::-4]);
copy=string[:]
print(copy);
copy=string[0:2]
print(copy);
copy=string[2:7];
print(copy)
copy=str(string);
print(copy)
copy=""+string;
print(copy)
text="credence automation testing";
print(text.capitalize());
print(text.casefold());
print(text.find('e',0,5));
print(text.find('auto',6,20));
print(text.islower());
print(text.isupper());
print(text.endswith("testing"));
print(text.find("auto"));
print(text.index('c',1));
