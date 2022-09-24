percent = 1.071
deposit = float(input())

year = 0
while (deposit < 700000):
    deposit *= percent
    year += 1
print(year)