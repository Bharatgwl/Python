import random

random_set = set()
while len(random_set) < 10:
    random_num = random.randint(1, 100)
    random_set.add(random_num)
print(random_set)
mylist = list(random_set)
for i in range(len(mylist)):
    if mylist[i] % 2 == 0:
        print(mylist[i])
    else:
        print("odd")
   