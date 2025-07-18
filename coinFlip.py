import random
heads=0
for i in range(1,100001):
    if random.randint(0,1) == 1:
        heads +=1
    if i == 500:
        print("Halfway done!")
print(f"heads came up {heads} times!")