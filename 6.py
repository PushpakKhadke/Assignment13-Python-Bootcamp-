"""
6. Write a python program to append elements from another list to the current list.(
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] )
"""

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
print(firstlist)
print(secondlist)
print("Append List:")
firstlist.append(secondlist[0])
firstlist.append(secondlist[1])
firstlist.append(secondlist[2])
print(firstlist)

"""
# 2nd Way!

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
firstlist.extend(secondlist)
print(firstlist)
"""