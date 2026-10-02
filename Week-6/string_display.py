str=input("enter a string: ")
uppercase=0
digit=0
lowercase=0
alphabet=0

for ch in str:
    if ch.isupper():
        uppercase+=1
        alphabet+=1
    elif ch.islower():
        lowercase+=1
        alphabet+=1
    elif ch.isdigit():
         digit+=1
print("number of uppercase: ",uppercase)
print("number of lowercase: ",lowercase)
print("number of digit: ",digit)
print("number of alphabet: ",alphabet)