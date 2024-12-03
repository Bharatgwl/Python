my_str = "hello ! how are you"
print(my_str)
print(type(my_str))
mylist = [1, "a", 2, "c"]
print(mylist)
print(type(mylist))
mytuple = (1, 2, 3, "r")
print(mytuple)
print(type(mytuple))
a = True
print(a)
print(type(a))
mydict = {'name1': "bharat", 'name2': "archit", 'name3': "deepanshu"}
print(mydict)
print(type(mydict))
myset = {1, 2, 3, 3, 3, 3, 4, 5}
print(myset)
print(type(myset))
myset1 = set()
myset1.add(1)
myset1.add(2)
myset1.add((1, 2))
print(myset1)
for i in range(6):
    myset1.add(i)
print(myset1)
myset2 = set([1, 'd', 3, 'z', 3, 3, 4, 0])
print(myset2)
if 2 in myset2:
    print(f"yes {2} is present int set")
else:
    print("no 2 is not present in the given sets ")   
print(mydict['name1'])