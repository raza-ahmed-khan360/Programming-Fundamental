for i in range(1,3):
    for j in range(1,3):
        print(f"i={i}, j={j}", end=" ")
    print()

for i in range(1,4):
    for j in range(1,4):
        print(f"{i} x {j} = {i*j}", end=' ')
    print()

for i in range(1,6):
    for j in range(1,6):
        print(f"{i*j:4d}", end=" ")
    print()
    
for i in range(1,11,2):
    for j in range(1,11,2):
        print(f"{i*j:4d}", end=" ")
    print()
    

for i in range(1,11,2):
    for j in range(2,11,2):
        print(f"{i*j:4d}", end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(f"{i*j:4d}", end=" ")
    print()

for i in range(1, 11):        
    fact = 1
    for j in range(1, i + 1): 
        fact = fact * j
    print(f"{i}! = {fact}")

for i in range(1,6):
    for j in range(1,6):
        print(f"{i}", end=" ")
    print()
    
for i in range(1,6):
    for j in range(1,6):
        print(f"{j}", end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        print(f"{i+j}", end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        print(f"{i*j}", end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        print(f"{chr(i+64)}{chr(i+96)}", end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        print(f"{chr(j+64)}{chr(j+96)}", end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(f"{chr(j+64)}{chr(j+96)}", end=" ")
    print()

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(f"{chr(j+64)}{chr(j+96)}", end=" ")
    print()

    