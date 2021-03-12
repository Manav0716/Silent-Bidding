#import clear
from replit import clear
from art import logo
print(logo)

bids={}
n='yes'
while(n!='no'):
    name=input("enter your name")
    bid=int(input("enter your bid")) 
    bids[name]=bid
    n=input("you want to continue")
    clear()
#print(bids)
max=0
for bidder in bids:
    value=bids[bidder]
    #value=int(value)
    if value>max:
        max=value
        winner=bidder
print(f"the winner of this bid is {winner}")
        

