import random

# Computer choice
computer=random.choice([1,2,3])

# User input
youstr=input("Enter s for stone,p for paper and x for scissor: ")

# Dictionaries
youdict={"s":1,"p":2,"x":3}
revdict={1:"stone",2:"paper",3:"scissor"}

if( youstr not in youdict):
    print("Invalid choice!")
else:
    you=youdict[youstr]
    print(f"You chose {revdict[you]}\n Computer chose {revdict[computer]}")
    
    if(computer==you):
        print("Draw")
    elif(computer==1 and you==2 ):
        print("You won")
    elif(computer==1 and you==3 ):
        print("You lose")
    elif(computer==2 and you==1 ):
        print("You lose")        
    elif(computer==2 and you==3 ):
        print("You won")
    elif(computer==3 and you==1 ):
        print("You won") 
    elif(computer==3 and you==2 ):
        print("You lose")