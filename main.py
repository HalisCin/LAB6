
# Question 1

function = lambda n: (n-3)/n**2

number=int(input('Please give a number : '))

functionList=[]

for i in range(1,number+1,1):
    functionList.append(function(i))

print(sum(functionList))

# Question 2

def recursive(n):

    if n == 0:
        return 1
    else:
        return ((n / (n + 2)) - 10) * recursive(n - 1)


number2 = int(input("Please enter another number: "))
print(recursive(number2))








