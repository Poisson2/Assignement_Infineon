import random as rd

for i in range(1,101):
    rand = rd.randint(1,100)
    ln = ""
    if(rand%7 == 0):
        ln = "lucky number!"
    print(i, rand, ln)
    if(i%5 == 0):
        print("---")
    
    