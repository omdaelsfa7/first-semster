#1
""" 
def stirng_coungter(string1):
    l1=string1.split()
    counter=0
    for i in l1 :
        for j in i:
            counter+=1
    print(l1)
    return counter
x=input("please enter the string")
print(stirng_coungter(x))       """
#2 
"""def count(string1):
    vowcounter=0
    numcounter=0
    constcounter=0
    l1=[1,2,3,4,5,6,7,8,9]
    strip_chars = "@"
    string1=string1.replace(strip_chars,"")
    vowels=["a","e","i","u","o"]
    print(string1)
    for i in string1:
        if i.lower() in vowels:
            vowcounter+=1
        elif i.isdigit() :
            numcounter+=1 
        else:
            constcounter+=1 
    print("vowcounter=",vowcounter)   
    print("numcounter=",numcounter)     
    print("constcounter=",constcounter)  
    return None
x=input("enter your shoit")
count(x)"""""
#3
""""user_input = input("Enter a string: ")

arranged_string = ''.join(sorted(user_input, key=lambda x: (x.isupper(), x.isnumeric(), x)))

print(f"The arranged string is: {arranged_string}")"""""
#or
"""def z(str1):
    lowerl=[]
    upperl=[]
    for i in str1:
        for j in i :
            if j.islower():
                lowerl.append(j)
            else:
                upperl.append(j)

    x="".join(lowerl+upperl) 
    return(x)
y=input("enter the string  ")     
print(z(y))"""""
#4
"""def rev(snt):
    l1=snt.split()
    for i in range(len(l1)) :
        l1[i]=l1[i][::-1]               #revword=[word[::-1] for  word in l1 ]
    sentce=" ".join(l1)  
    return(sentce)
x=input("enter the sentence")       
print(rev(x))   """""
#5
"""def y(xlist):
    l2=[]
    l2=list(dict.fromkeys(xlist))
    return (l2)
l2=[]
for i in range(5):
    i=input("enter the list num")
    l2.append(i)

print(y(l2))"""
#or
"""def y(mylist):
    i=0
    while i <len(mylist)  -1 :
        if mylist[i]==mylist[i+1]:
            mylist.pop(i)
            print(mylist)
        else:
            i+=1    
    return mylist
l2=[]
for i in range(5):
    i=int(input("enter the list num"))
    l2.append(i)
print(y(l2)) """    
#6
"""pass"""""
#7
"""def gcd(x,y):
    j=x%y
    return j 
q=int(input("enter first number"))
w=int(input('enter the second number'))
print(gcd(q,w))"""
#8
"""def calc(q,w,e):
    if q=="*":
        result= w * e 
    elif q=="/" :
        result = w / e 
    elif q =="+":
        result = w + e 
    elif q =="-" :
        result = w - e 
    else:
        result = "enter valid opreator "             
    return result 
z=input("enter the opreator")
x=eval(input("enter the second num"))
c=eval(input("enter the num"))
print(calc(z,x,c))"""
#9 
"""def cap(file):
    x=open( file , "r")
    content=x.readlines()
    for i in range (len(content)):   
        content[i]=content[i].title()
    y="".join(content)
    print(y)   
    x.close()
    return None
j=input("enter the file:")
print(cap(j))"""""
#10
"""def remove(file):
    remove= ["#","@","/","*"]
    x=open(file , "r")
    content=x.readlines()
    for i in range(len(content)):
        for j in content[i]:
            if j in remove:
                content[i] = content[i].replace(j, "")
    y=open(file ,"w")
    y.writelines(content)
    y.close()
    return None 
j=input("enter file name")
print(remove(j))"""      
#or omar helal 7al
"""x=open("file1.txt","r")
content=x.read()
y=["@","!"]
for i in y :
    content=content.replace(i ,"")
x=open("file1.txt","w")
x.writelines(content)
print(content)
x.close()"""
#11
"""def cou(file):
    x=open(file , "r")
    content=x.readline()
    counter=0
    for i in content :
        if i.isupper():
            counter+=1
    return counter
x=input("file:")
print(cou(x))"""  
#12
"""def hah(l1):
    x="\n".join(l1)
    file=open("file1.txt" , "w")
    file.write(x)
    z="done"
    return z
list1=["omar","helal",'helal']
print(hah(list1))"""
 #13
"""def char(file):
    l1=[]
    for i in file:
        f=open(i ,"r")
        content=f.readline()
        for j in content:
            l1.append(j)
    return l1
x=["file1.txt","file2.txt"]
print(char(x))"""
#14 
"""def unique(file):
    f= open(file,"r")
    unique_words=set()
    content=f.readlines() 
    print(content)  
    for line in content:
        words = line.split()
        for word in words:  
            word = word.lower()
            unique_words.add(word)
    return unique_words  
filee=input("file:")    
print(unique(filee))"""
#15 
"""def di(students,grades):
    studentdict=dict()
    for i in range (len(students)):
        studentdict[students[i]]=grades[i]
        print(studentdict) 
        i=0
        for j in studentdict.values():
            i+=j
        avg=i/len(studentdict)       
    return avg
students=["omar","emad","mohamed"]
grades=[50,60,70]
print(di(students,grades))"""
#16 
"""def tu(tuq,factor):
    modfuple=tuple()
    for i in tuq:
        modfuple += (i*factor,)
    return(modfuple)
tuq=(2,3,4)   
factor=5
print(tu(tuq,factor))"""
#17
"""def checker(dict , key):
    result="key does not exist"
    for i in dict.keys():
        if key == i:
            result="key exist"
        else:
            continue   
    return result
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
key='age'
print(checker(my_dict,key))"""
#18
"""def fun(x):
    list1=x.split()
    long_Word=""
    counter=0
    for i in range(len(list1)):
        if len(list1[i]) > counter :
            counter=len(list1[i])
            long_Word=list1[i]
        else:
            continue 
    return long_Word  
input_text = "Python is a powerful programming language with a simple syntax."
print(fun(input_text))"""
#19
"""def conc(tuple1,tuple2):
    conctuple=tuple()
    conctuple=tuple1+tuple2
    return conctuple
tuple1=(1,2,3)
tuple2=(4,5,6)
print(conc(tuple1,tuple2))"""
#20
"""def inter(set1,set2):
    intersection_set=set()
    intersection_set=set1.intersection(set2)
    l1=[]
    l1=list(intersection_set)
    return l1
set1={1,2,3}
set2={3,4,5,2}
print(inter(set1,set2))"""
#21
#22
"""x=int(input("num1:"))
y=int(input("num2:"))
z=(x/y)
z=str(z)
l=z.split(".")
for i in range(len(l)):
    l[i]=int(l[i])
    print(l)
    
print(eval(z)+x) """       
#23
"""a=int(input("numa:"))
b=int(input("numb:"))
print(a,b)
l=[]
l.append(a)
l.append(b)
a=l[1]
b=l[0]
print("numa=",a)
print("numb=",b)"""
#24
#25
"done before"
#26
"""x=input("enter the word")
y=x.title()
print(y)"""
#27
"""def hipster(blue,red):
    diffrent_socks=0
    same_redsocks=0
    same_bluesocks=0
    a=0
    while red != 0 and blue != 0 :
        diffrent_socks+=1
        red-=1
        blue-=1 
    while red>=2   :
        if red>1:
            red -=2
            same_redsocks +=1
    while blue>=2  :
        if blue >1 :
            blue -=2
            same_bluesocks +=1
    if same_bluesocks >same_redsocks:
        a=same_bluesocks 
    else:
        a=same_redsocks          
    return diffrent_socks , a 
x=int(input("blue:")) 
y=int(input("red:")) 
print(hipster(x,y))"""
#28
"""def fun(x,y,z,c):
    l=x*y*z*c
    l=str(l)
    return l[-2]+l[-1]
x=5
y=2
z=7
c=4
print(fun(x,y,z,c))"""
#29
"""def fun(z,x,q,w):
    l1=[z,x,q,w]
    l1.sort()
    print(l1)
    m=l1[1]
    n=l1[2]
    if l1[1]<l1[2]:
        m=-1
        n=""
    return m,n
f=2
g=5
h=6
j=12
print(fun(f,g,h,j))"""
#30
"""q=int(input("the number "))
w,e=int(input("enter the interval")),int(input("ente the interval"))
r,t=int(input("enter the interval")),int(input("ente the interval"))
y,u=int(input("enter the interval")),int(input("ente the interval"))
l1=[]
l2=[]
l3=[]
counter=0
l1.append(w)
l1.append(e)
l2.append(r)
l2.append(t)
l3.append(y)
l3.append(u)
x=""
y=""
z=""
if q>l1[0] and q<l1[1]:
    counter +=1
    x=l1
if q>l2[0] and q<l2[1]:
    counter+=1  
    y=l2
if q>l3[0] and q<l3[1]:
    counter+=1
    z=l3
print("number",q,"is in",counter,x ,y,z)"""   
#31
"""l1=[1,2,3,4,5,6,7]
counter=0
for i in l1:
    counter+=i    
print(counter)    
"""
#32
"""def watermelon(x):
    if x%2==0 and x>2:
        x=("yes")
    else:
        x=("NO")
    return x
x=int(input("hm kilos"))               
print(watermelon(x))"""
#33
"""def x(num,word):
    if len(word)>=num:
        x=str((len(word)-2))
        j=word[0]+x+word[-1]
        
        
        
    else:
        j=word
    return j 
l=int(input("number of max char:"))
q=input("the word:") 
print(x(l,q))"""   


#37
"""def fun(num):
    l1=[]
    num=str(num)

    for x in num:
        l1.append(x)

    for i in range(10):
        counter =0
        for j in l1:
            if str(i)==j:
                counter+=1
        print(i,counter)    


    return            
print(fun(11123))"""
#38
"""def fun(num):
    l1=[]
    num=str(num)
    for i in num:
        l1.append(i)
        max_counter=0
        x=""
    for j in range(len(l1)):            not done 
        counter=0
        for x in l1:
            if str(j)==x: 
                        
        if counter>max_counter:
            max_counter=counter

    return max_counter ,
print(fun(5551)) """      
#39
"""from  math import  ceil
def fun(length,width,square):
    x=ceil(length/square)
    y=ceil(width/square)  
    return (print(x*y))
fun(6,6,4)"""
#40
"""def rucabman(num):
        l1=list(num)
        for i in range(len(l1)):
        v=l1.index(l1[-1])
        q= l1[-1] - v -1
        z= l1[-1] + v + 1 

        if q  not in  l1  and q != 0 :
            l1.insert(v+1 ,q)
        else:
            l1.insert(v+1,z)    
        if l1[-1] == 43:
            
rucabman([0,1,3,6,2,7])
"""
