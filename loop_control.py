#Loop control statement

count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
         break #exit count when number reached.
     
    fruits = ["Apple","Banana","Cherry","Date"]

for fruit in fruits:
    if fruit == "Cherry":
        break#Exit the loop if cherry is found
    print(fruit)
    
    print()
for fruit in fruits:
    if fruit == "Cherry":
        continue #Skips cherry and moves to the iteration
    print(fruit)