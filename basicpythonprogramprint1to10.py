# for i in range  (0,10):
#     print(i)

# sum of 100 numbers
# for i in range  (0,100):
#     print(i+1)

# sum of two numbers
# a=5;
# b=10;
# sum=a+b
# print(sum)

# how can you write fibonnoci series using python

n=100
a=0
b=1
for i in range (n):
    print(a)
    a,b=b,a+b


# How can you write factorial of number

n = 5
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)


    
#check even or odd

for i in range (1,100):
    if (i%2)==0:
        print(i, "is even")
    else:
        print(i, "is odd")
