print("Welcome to Samarthya Pizza")
bill=0
print("What size of pizza do you want?")
Size=input("Small(S)/Medium(M)/Large(L)")
if(Size=='S'):
    bill=3
elif(Size=='M'):
    bill=5
elif(Size=='L'):
    bill=10
else:
    print("Error")
    exit 
print("Do you want extra pepporoni?")
print("Type (Y or y) for Yes or (N or n) for No")
extrap=input(" Yes(Y)/No(N)")

if(extrap=='Yes' or extrap=="Y"):
    bill+=1.5
print("Do you want extra Sauce?")
print("Type (Y or y) for Yes or (N or n) for No")
extraSauce=input("Yes(Y)/No(N)")

if (extraSauce=='Y' or extraSauce=="yes"):
    bill+=1.5 

print("Your Final amount is",bill)

        