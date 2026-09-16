num=int(input("enter a number :"))

original=num
reversed=0

while num>0:
    digit=num%10
    reversed=reversed*10+digit
    num=num//10
    
if original==reversed:
    print("Number is palindrome!")
else:
    print("Number is not palindrome!")