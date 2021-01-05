# Fibonacci Sequence - Enter a number and have the program generate the
# Fibonacci sequence to that number or to the Nth number.

n = int(input("n: "))

fibonacci = [0, 1]

for i in range(0, n, 1):
    next = fibonacci[i] + fibonacci[i+1]
    fibonacci.append(next)

print("Fibonacci: ", fibonacci[:-2])
