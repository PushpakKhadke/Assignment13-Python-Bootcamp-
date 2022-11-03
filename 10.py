"""
10. Write a Python script to create a list, where each element of the list is a digit of a
given number.
"""

List=[]
Number=int(input("How Many Number You Want Enter : "))
while Number:
    List.append(input("Enter NUmber : "))
    Number-=1
print(List)




"""
2nd Way!

a1 = input("Enter Number : ")
a2 = input("Enter Number : ")
a3 = input("Enter Number : ")
a4 = input("Enter Number : ")
a5 = [a1,a2,a3,a4]
print(a5)
"""