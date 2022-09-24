quantity_of_atoms = int(input())
final_quantity_of_atoms = int(input())

days = 0
while (quantity_of_atoms >= final_quantity_of_atoms):
    quantity_of_atoms /= 2
    days += 1

result = days * 12
print(result)