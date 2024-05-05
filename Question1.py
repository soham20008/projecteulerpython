# Find the sum of the multiples of 3 or 5 below the provided parameter value number.
# Question number 1(Project Euler)


# code here

n =  int(input("Type your limit here: "))
sum = 0

for i in range(1,n):
    if i%3 == 0 or i%5 == 0:
        sum = sum + i
print(sum)

