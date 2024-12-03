# # def fibonacci(n):
# #     if n <= 1:
# #         return n
# #     else:
# #         return fibonacci(n - 1) + fibonacci(n - 2)
# # n = int(input("Enter the number of terms: "))
# # print(f"Fibonacci sequence up to {n} terms:")
# # for i in range(n):
# #     print(fibonacci(i
# print("hello namit")
# age=int(input("enter your age"))
# if age>=18:
#     print("you can vote")
# else:
#     print("you cannot vote")


file = open("hello.txt", "w")
text = file.write("hi how are you")
with open("hello.txt", "r") as file:
    print(file.read())
file.close()
