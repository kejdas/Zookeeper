n = int(input())

counter = 1

while n in range(1,100):
    counter = counter * n
    n -= 1
print(counter)