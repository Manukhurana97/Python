#regular expression
import re

# find name and age of all
Nameage = '''
Manu is 21 and Khurana is 22
Abc is 18 years 
'''
names = re.findall(r'[A-Z][a-z]*', Nameage)
ages = re.findall(r'\d{1,3}', Nameage)
agedicl={}
x=0
for eachname in names:
    agedicl[eachname]=ages[x]
    x+=1
print(agedicl)



# find the name ones
if re.search("hello","my name is hello"):
    print("hello is present")



# find the inform multiple times
demo=re.findall("inform","inform saurabh the i have given information to every one ")
for inform in demo:
    print(inform)



# find the postion for inform
str=re.finditer("hello","hello to all ,hello how are you")
for i in str:
    list =i.span()
    print(list)



#matching words with particular pattern
str="Sat,mat,pat,rat"
matchstr=re.findall("[smpr]at",str)
for i in matchstr:
    print(i)

# replace a string
str="Sat,mat,pat,rat"
regex=re.compile("[r]at")
str =regex.sub("bat", str)
print(str)



#wide spaces
str='''hello
how are you
i am fine'''
print(str)
regex=re.compile("\n")
str=regex.sub(" ",str)
print(str)



# Calculate the length
num='12345'
num=len(re.findall("\d{1}",num))
print(num)

# Calculate the length of particular range
num="1,12,123,1234,12345,123456,1234567"
num=len(re.findall("\d{5,7}",num))
print(num)



# correct mobile no finding problem
# \w -> {a-z A-Z 0-9}
# \W -> {^a-z A-Z 0-9} search except all these
# correct mobile no finding problem
# \w -> {a-z A-Z 0-9}
# \W -> {^a-z A-Z 0-9} search except all these
name=input("enter your full name (firstname lastname ) :")
if re.search(r"[A-Z][a-z].{2,30}\s\w{2,30}","name"):
    print("this is correct name")
else:
    print("Keep the first letter as capital and Insert the space between first and the last name")
phone="(91)123-456-7890"
if re.search("\(\d{2}\)\w{3}-\w{3}-\w{4}",phone):
    print("This is correct phone no")
else:
    print("its not a correct no")
email=input("Enter email id:")

if re.search(r"[A-Za-z]*@gmail.com",email):
    print("correct email ")
else:
    print("incorrect")
