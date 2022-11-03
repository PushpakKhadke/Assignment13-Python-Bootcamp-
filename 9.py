"""
9. Write a Python script to create a list of city names taken from the user.
"""


List=[]
Number=int(input("How Many City You Want Enter : "))
while Number:
    List.append(input("Enter City Name : "))
    Number-=1
print(List)

"""
2nd Way!
a1 = input("Enter City Name : ")
a2 = input("Enter City Name : ")
a3 = input("Enter City Name : ")
a4 = input("Enter City Name : ")
a5 = [a1,a2,a3,a4]
print(a5)
"""
