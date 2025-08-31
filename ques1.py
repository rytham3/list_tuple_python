# Write a program to store seven fruits in a list entered by the user.


fruits = []


for x in range(7):
    fruit = input(f"Enter fruit name {x+1}: ")
    fruits.append(fruit)

print(fruits)
    