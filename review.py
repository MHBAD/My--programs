##ex1
txt="I love apples , apples are my favrite fruit - apple"
x=txt.find("apple")
print(13 , "find ()" ,x)
## ex14
txt="I love apples , apples are my favrite fruit - apple"
x=txt.find("manaf")
print(14 , "find ()" ,x)
## ex15
txt="I love apples , apples are my favrite fruit - apple"
x=txt.find("m")
print(15 , "find ()",x )
##ex4
txt="Hello , welcome to our course"
x=txt.index("e",5,10)
print(5 , "index ()",x)
##ex5
## ex7

txt="Hello , welcome to our course."
x=txt.endswith(".")
print(7 , "endswith ()",x)
## ex 10
txt="Hello , welcome to our course."
x=txt.endswith("our course.",5,10)
print(10 , "endswith ()",x)
##ex9
txt="Hello , welcome to our course."
x=txt.islower()
print(12 , "islower ()",x)
##ex2
## ex14
a="hello 123"
b="myHasan"
aa=a.islower()
bb=b.islower()
print(14 , "islower ()",aa)
print(14 , "islower ()",bb)
## ex15
## ازل المسافات على القسم الأيسر من السلسلة
txt="            banana            "
print(15,"lstrp()" ,txt)
x=txt.lstrip()
print(15,"lstrp()" ,x)
## ex16
txt=",,,,,banana.....apple"
x=txt.lstrip()
print(16,"lstrp()" ,x)
## ex17
txt=",,,,,banana.....apple"
x=txt.lstrip(",.")
print(17,"lstrp()" ,x)
## ex18
txt=",,,,,.....banana.....apple"
x=txt.lstrip(",.")
print(18,"lstrp()" ,x)
## ex19
txt=",,,,,.....banana.....apple"
x=txt.lstrip(",")
print(19,"lstrp()" ,x)
## ex20
txt=",,,,,..aab...banana.....apple"
x=txt.lstrip(",.a")
print(20,"lstrp()" ,x)
##ex21
txt=",,,,,..aab...bananas.....apple"
x=txt.partition("bananas")
print(21,"partition()" ,x)
## ex 22 
txt=",,,,,..aab...bananas.....apple"
x=txt.partition("yes")
print(22,"partition()" ,x)
## ex 23 
txt=",,,,,..aab...bananas.....apple"
x=txt.partition("apple")
print(23,"partition()" ,x)
##ex7
mytuple=("Abd","jaber","ismail")
x=" ,".join(mytuple)
print(1,"join()",x)
##ex23
mytuple=("Abd","jaber","ismail")
x=" ++".join(mytuple)
print(2,"join()",x)
## with dic
myDic={"name":"Bha","country":"Syria"}
mySeprtor="TEST"
x=mySeprtor.join(myDic)
print(3,"join()",x)
##ex4
txt="Hello , welcome\n to our course."
x=txt.splitlines()
print(4 , "splitlines ()",x)
# ex5
txt="Hello , welcome to our course."
x=txt.startswith("Hello")
print(5 , "startswith ()",x)
# ex10
txt="Hello , welcome to our course."
x=txt.swapcase()
print(10 , "swapcase ()",x)
## ex12
txt="Hello , welcome to our course."
x=txt.title()
print(12 , "title ()",x)
## ex 13
print(13-1,10>9)
print(13-2,10==9)
print(13-3,10<9)
## ex 14
print("13-1",10>9)
print("13-2",10==9)
print("13-3",10<9)
##ex15
a=200
b=33
if b>a :
    print("2 ex if = true" )
else:
    print("2 ex  if = false" )
## ex3 
print("ex3",bool("Hello") )
print("ex3",bool(15) )
## ex1
## التأكد فيما اذا كان الكائن نوعه صحيحا أو لا
x=150
y=250.2
print("ex1 x", isinstance(x,int))
print("ex1 y", isinstance(y,int))
##ex4

x=10
y=5
z=3.5
g=12
h=4


sume=x+y
sub=x-h
mul=x*g
div=g/h
modd=g%h
expon=y**h
dddfloor=g//y
print("x=10 ,y=5, z=3.5 , g=12 ,h=4 ")
print("ex4 :sume=x+y","sum =" ,sume)
print("ex4:sub=x-h","sub =" ,sub)
print("ex4 :mul=x*g","mul =" ,mul)
print("ex4 :div=g/h","div =" ,div)
print("ex4 :modd=g%h","modd =" ,modd)
print("ex4: expon=y**h","expon =" ,expon)
print("ex4: dddfloor=g//y","dddfloor =" ,dddfloor)
##ex3
## ex1
print("ex1", 5+4-7+3)
## ex3
y=z=b=j=2 
y,z,b,n,j=2,2,1,1,2 
x= y * z + n * j / b ** 2 + (y+z)
print("ex3", x)
##ex7
names=["ismail","sedra","maan","jaber","manaf","abd alfattah"
       ,"hussam","obai","hith","bhaa","lama","ahmad"]
print("ex7",names[2:4])
##ex8
names=["ismail","sedra","maan","jaber","manaf","abd alfattah"
       ,"hussam","obai","hith","bhaa","lama","ahmad"]
print("ex8",names[0:5])
print("ex8",names[:5])
print("ex9",names[4:])
#ex10
names=["ismail","sedra","maan","jaber","manaf","abd alfattah"
       ,"hussam","hith","bhaa","lama","ahmad"] 
print(names)    
names[7]="gaith"
print(names)   
##ex13
## تبديل قيمة عنصر بثلاثة قيم 
cars=["bmw","ford","marcedece"]
print(cars)   
cars[1:2]=["ford1","ford2","ford3"]       
print(cars) 
##ex5
x=[1,2,3]
y=[1,2,3]
x=y
print (x is y) 
print (x is x) 
print (x is not y) 
## ismail
f = ["ford", "bmw", "dodge"]
s = ["ford", "bmw", "dodge"]
z = f

print(f is z)
##ex5
office=["Word","Excel","power point"]
i=0
while i < len(office):
    print(office[i])
    i=i+1
##ex7
office=["Word","Excel","power point"]
newlist=[]
for x in office:
    if "o" in x:
        newlist.append(x) 
print(newlist)        
##ex9
office=["Word","Excel","power point"]
newlist=[]
i=0
while i < len(office):
    if "o" in office[i]:
        newlist.append(office[i]) 
    i=i+1
print("ex9",newlist)  
## ex 10
office = ["word", "excel", "power point"]
newlist = [x for x in office if x != "power point" ]
print(newlist)
## ex11
newlist2 = [x for x in range(10)  ]
print(newlist2)
## ex12
newlist2 = [x for x in range(10) if x<=5 ]
print(newlist2)
##append()
office1 = ["word4", "excel"]
office2 = [ "power point","access"]

for x in office2:
    office1.append(x)

print(office1)
##ex5
office = ["word3", "excel", "power point","access"]
office2=list(office)
## ex11
office = ["word", "excel", "power point","access"]
office.sort()
print(office)
##ex5
def myfun(n):
    return abs(n-50)

numlist=[100,50,65,82,23,1]
numlist.sort(key=myfun)
print(numlist)
## ex6
officenum = [1,2,3,5,-8,-6,-1,0]
officenum.sort()
print(officenum)
## ex7
officenum = [1,2,3,5,-8,-6,-1,0]
officenum.sort(reverse=True)
print(officenum)
##ex8
office = ["word", "excel", "power point","access"]
newlist2 = [x.upper() for x in office ]
print(newlist2)
## ex13
courses=("python","python","python","machin learning","al")

x=courses.count("python")
print("ex13",x)
##ex6
marks=(5,6,7,8,87,4,5,4,7,3,2,1,4,2)
dic={}
for i in marks:
    if i in dic:
       dic[i]+=1
    else:
        dic[i]=1
for i, count in dic.items():
    print(f"{i}:{count}")
## ex15
marks=(3,6,7,8,8,7,4,5,4,7,3,2,1,4,2)

x=marks.index(5)
print("ex15",x)
##ex9
courses=set(("python","python","machin learng","surface","tensorflow"))
for x in courses:
      print("ex23","surface" == x)
##ex24
courses=set(("python","python","machin learng","surface","tensorflow"))

print("ex24","surface" in courses)
##ex6
dictionary={
    "brand":"BMW", 
    "model":True,
    "year":2015,
    "colors":["red","blue","black"]
}
x=dictionary["brand"]
print("ex8 ",type(dictionary),x)
##ex9
## access to elements
dictionary={
    "brand":"BMW", 
    "model":True,
    "year":2015,
    "colors":["red","blue","black"]
}
x=dictionary.get("year")
print("ex9 ",type(dictionary),x)
##ex10
## access to elements
dictionary={
    "brand":"BMW", 
    "model":True,
    "year":2015,
    "colors":["red","blue","black"]
}
x=dictionary.values()
print("ex10 ",x)
##ex4
n1 = "game, over"
print(n1[-8:-2])
##ex5
txt9 = "Hello , world!"
print(txt9.split("o"))
##ex6
x5 ="nice"
def myfunc5():
    global x5
    x5="great5"

print("python is 5" + x5)   

myfunc5()

print("python is 5" + x5) 


