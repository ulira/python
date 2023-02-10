#if statement
x=1
marks=49
grade=-3
days="january"
if(x>0):
    print("The number is positive")
# if ...else statement
if(marks>=50):
    print("you have passed the exam")
else:
    print("you have failed")

# if..elif(else if)..else statement
if(grade>=29 and grade>=0):
    print("you have failed")
elif grade>=30 and grade<=49:
    print("you have passed")
elif grade>=50 and grade<=79:
    print("you have a credit")
elif grade>=80 and grade<=100:
    print("you have a distinction")
else:
    print("wrong grade entered")

if days=="thursday":
    print("buy two icecream get one free")
elif days=="tuesday":
    print("half prize if you buy more than 1 pizza")
elif days=="wednesday":
    print("burger wednesday")
elif days=="monday":
   print("java monday")
elif days=="friday":
   print("friends friday")
elif days=="saturday":
   print("super sato")
elif days=="sunday":
   print("family sunday")
else :
 print( "what day of the week is this")





