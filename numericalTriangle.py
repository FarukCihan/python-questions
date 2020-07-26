"""You are given a positive integer N. Print a numerical triangle of height N-1"""

num = int(input("Enter a number : "))
for i in range(1, num):
    print(i * str(i))
